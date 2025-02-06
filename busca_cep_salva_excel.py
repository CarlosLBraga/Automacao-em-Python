import http.client
import pandas as pd
import json


def obter_endereco_cep (cep):
    conexao = http.client.HTTPSConnection("viacep.com.br")
    conexao.request("GET", f"/ws/{cep}/json")
    resposta = conexao.getresponse()


    #o status HTTP 200 indica sucesso na requisição http
    #qualquer status diferente indica erro na solicitação
    if resposta.status != 200:

        #encerra a conexão e retorna None para indicar que a requisição
        #não foi bem sucedida
        conexao.close()
        return None
    


    #lê dados e os retorna em forma de bytes
    #precisa ser decodificada para string antes de ser convertida de JSON
    dados = resposta.read()
    endereco = json.loads(dados.decode("utf-8"))

    #encerra conexão https com o serv viacep, libera os recursos
    conexao.close()

    return endereco if "erro" not in endereco else None



#caminho do arquivo
caminho_planilha = "CEP.xlsx"



#a função "read_excel" carregar a aba 'CEP' do arquivo
planilhas_ceps = pd.read_excel(caminho_planilha, sheet_name='CEP')

#remove linhas que estão nulas
ceps = planilhas_ceps['CEP'].dropna()


#cria um novo dataframe com as colunas especificadas
resultados = pd.DataFrame(columns=['CEP', 'Logradouro', 'Bairro', 'Localidade', 'UF', 'DDD'])

for cep in ceps:

    endereco = obter_endereco_cep (str(cep).replace('-', ''))
    
    if endereco:
        nova_linha = pd.DataFrame([{
            'CEP': cep,
            'Logradouro': endereco.get('logradouro', ''),
            'Bairro': endereco.get('bairro', ''),
            'Localidade': endereco.get('localidade', ''),
            'UF': endereco.get('uf', ''),
            'DDD': endereco.get('ddd', ''),

        }])

        #o dataframe 'resultados' que foi inicializado fora do lopp é atualizado
                    #então inclui uma nova linha
        #a função 'pd.concat' é usada para concatenar a 'nova_linha' ao dataframe 'resultados'
        #'ignore_index=True' é importante para instruir o pandes a reindexar o dataframe resultante
                #indices serão renumerados de forma contínua, evita duplicação de colunas
        resultados = pd.concat([resultados, nova_linha], ignore_index=True)




#parte do código responsável por salvar os dados coletados
#'ExcelWriter' escreve em arquivos Excel
#'caminho_planilha' arquivo excel que escrito
#"engine='openpyxl' biblioteca usada para trabalhar com arquivos xlsx
# 'mode=a' configura o ExcelWriter para abrir o arquivo no modo de anexação ('a' de append)
#  importante para as abas existentes no arq. Excel não sejam excluídos
# 'sheet_name=Dados' mostra aonde os dados devem ser salvos "

with pd.ExcelWriter (caminho_planilha, engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
    resultados.to_excel(writer, sheet_name='Dados', index=False)

print("Endereços Salvos na aba 'Dados' da Planilha ")








