import http.client
import json
import pandas as pd

def formatar_empresa (empresa):
    campos_de_interesse = ['cnpj', 'nome', 'telefone', 'email', 'logradouro', 'bairro', 'municipio', 'uf', 'cep', 'atividade_principal']
    dados_formatados = {campo: empresa.get(campo, '') for campo in campos_de_interesse}

    if 'atividade_principal' in empresa and empresa['atividade_principal']:
        dados_formatados['atividade_principal'] = empresa['atividade_principal'][0].get('text', '')

    return dados_formatados 


def limpar_cnpj (cnpj):
    return ''.join(filter(str.isdigit,cnpj))

def obter_dados_empresa_cnpj (cnpj):
    cnpj = limpar_cnpj (cnpj)
    conexao = http.client.HTTPSConnection('www.receitaws.com.br')

    conexao.request('GET', f"/v1/cnpj/{cnpj}")

    resposta = conexao.getresponse()
    print(f'processando cnpj {cnpj}: status {resposta.status}')

    if resposta.status != 200:
        conexao.close()

        return None
    
    dados = resposta.read()
    conexao.close()
    empresa = json.loads(dados.decode('utf-8'))

    if 'status' in empresa and empresa['status'] == 'ERRO':
        print(f'ERRO ao buscar dados para o {cnpj}: {empresa.get(" message", "sem mensagens")} ')

    
    return empresa


def salvar_dados_empresa_excel (resultados, nome_arquivo, nome_aba='Dados'):

    with pd.ExcelWriter(nome_arquivo, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
        try:

            worksheet = writer.book[nome_aba]
            start_row = worksheet.max_row
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=True)

        except KeyError:
            resultados.to_excel(writer, sheet_name=nome_aba, index=False, header=False, startrow=start_row)

caminho_panilha = 'CNPJ.xlsx'

planilha_cnpj = pd.read_excel(caminho_panilha, sheet_name='CNPJ', dtype={"CNPJ": str})

resultados = []
for cnpj in planilha_cnpj ['CNPJ'].dropna():
    print(f'lendo cpnj: {cnpj}')

    dados_da_empresa = obter_dados_empresa_cnpj(str(cnpj))

    if dados_da_empresa:
        dados_formatados = formatar_empresa(dados_da_empresa)

        resultados.append(dados_formatados)


if resultados:
    resultados_df = pd.DataFrame(resultados)

    salvar_dados_empresa_excel (resultados_df, caminho_panilha)

print("Dados Salvos com sucesso")


    
