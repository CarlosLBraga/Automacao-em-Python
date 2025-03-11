import pyautogui as serv
import threading
import keyboard



# Variável de controle para parar a execução
executando = True

def monitorar_tecla():
    "Interrompe o programa quando a tecla 'ctrl' for pressionada."
    global executando
    keyboard.wait('ctrl')  # Aguarda a tecla ser pressionada
    executando = False   # Altera a variável para interromper o loop
    serv.alert('PROGRAMA INTERROMPIDO')
    print("Execução interrompida pelo usuário!")

# Inicia a thread de monitoramento de tecla
thread_tecla = threading.Thread(target=monitorar_tecla, daemon=True)
thread_tecla.start()

def inicio_pag():
    if not executando: return
    serv.hotkey('ctrl', 'home')
    serv.hotkey('left')

def prox_pag():
    if not executando: return
    serv.hotkey('ctrl', 'TAB')

def prox_campo():
    if not executando: return
    serv.hotkey('TAB')

def copia():
    if not executando: return
    serv.hotkey('ctrl', 'c')

def cola():
    if not executando: return
    serv.hotkey('ctrl', 'v')

def espera_curta():
    if not executando: return
    serv.sleep(1.5)

def pag_anterior ():
    serv.hotkey('alt', 'left')


def confirma ():
    serv.hotkey('enter')

def percorre_campos (n):
    
    for i in range (n):
        prox_campo()

def aba_cadastro ():
    serv.click(x=536, y=353)
    percorre_campos(1)
    confirma()
    serv.sleep(3)
    percorre_campos(10)



def agendamento (hora):
    serv.sleep(5)

    percorre_campos(9)

    confirma()
    serv.sleep(4)

    percorre_campos(8)


    prox_pag()
    espera_curta()

    inicio_pag()
    copia()

    prox_pag()
    serv.sleep(2)
    cola()
    confirma()

    espera_curta()
    percorre_campos(3)

    espera_curta()

    for i in range (2):
        espera_curta()
        confirma()

    if not executando: exit()
    percorre_campos(2)
    serv.write('odontologia')
    espera_curta()
    percorre_campos(2)

    serv.write('Jose')
    serv.sleep(1)
    percorre_campos(1)
    confirma()
    percorre_campos(3)
    serv.sleep(1)
    serv.doubleClick(x=888, y=328)
    espera_curta()
    percorre_campos(1)
    if hora == '09:00':
        serv.write('900')
    elif hora == '18:00':
        serv.write('1800')
    
    percorre_campos(3)
    confirma()
    serv.sleep(2)
    percorre_campos(4)
    confirma()
    serv.sleep(2)
    percorre_campos(2)
    confirma()

def atendimento ():
    serv.sleep(5)
    percorre_campos(11)
    espera_curta()

    if not executando: exit()
    for i in range (2):
        espera_curta()
        confirma()

    percorre_campos(3)
    serv.hotkey('down')
    espera_curta()
    percorre_campos(4)
    confirma()

    serv.sleep(2)
    percorre_campos(2)
    confirma()

def dinheiro ():
    percorre_campos(4)
    serv.hotkey('space')
    percorre_campos(3)
    espera_curta()
    serv.write('2500')
    percorre_campos(1)
    serv.write('2500')
    percorre_campos(1)
    serv.write('taxa unica')

def debito ():
    percorre_campos(3)
    serv.hotkey('space')
    percorre_campos(4)
    espera_curta()
    serv.write('2500')
    percorre_campos(1)
    serv.write('2500')
    percorre_campos(1)
    prox_pag()
    espera_curta()
    inicio_pag()
    percorre_campos(9)
    copia()
    espera_curta()
    prox_pag()
    espera_curta()
    cola()
    percorre_campos(1)
    serv.write('taxa unica')


def credito ():
    percorre_campos(2)
    serv.hotkey('space')
    percorre_campos(5)
    espera_curta()
    serv.write('2500')
    percorre_campos(1)
    serv.write('2500')
    percorre_campos(1)
    prox_pag()
    espera_curta()
    inicio_pag()
    percorre_campos(9)
    copia()
    espera_curta()
    prox_pag()
    espera_curta()
    cola()
    percorre_campos(1)
    serv.write('taxa unica')


def pix ():
    percorre_campos(5)
    serv.hotkey('space')
    percorre_campos(2)
    espera_curta()
    serv.write('2500')
    percorre_campos(1)
    serv.write('2500')
    percorre_campos(1)
    prox_pag()
    espera_curta()
    inicio_pag()
    percorre_campos(9)
    copia()
    espera_curta()
    prox_pag()
    espera_curta()
    cola()
    percorre_campos(1)
    serv.write('taxa unica')








def pagamento (pag):
    serv.sleep(4)
    percorre_campos(9)
    serv.hotkey('space')
    espera_curta()

    #fução de pagamento

    if pag == 'Débito':
        debito()
    
    elif pag == 'Crédito':
        credito()
    
    elif pag == 'Pix':
        pix()
    
    else:
        dinheiro()

   
    percorre_campos(8)
    confirma()
    

    espera_curta()
    percorre_campos(2)
    confirma()

    espera_curta()
    percorre_campos(2)
    confirma

    espera_curta()
    prox_pag()

    if pag == 'Dinheiro':
        inicio_pag()
        espera_curta()
        for i in range(10):
            prox_campo()

        for i in range (2):
            espera_curta()
            confirma()  
    
    else:
        prox_campo()
        for i in range (2):
            
            espera_curta()
            confirma()

    espera_curta()
    prox_pag()
    espera_curta()

    
    




# Início da automação




serv.sleep(4)

usuario = serv.confirm('selecione o usuário da execução', buttons =['Cadu', 'Matheus'])

if usuario == 'Cadu':
    u = 'carlos.e.braga@kroton.com.br'
elif usuario == 'Matheus':
    u = 'matheus.lima@cogna.com.br'



inicio_pag()


# Pega o primeiro campo
for i in range(6):
    if not executando: break
    espera_curta()
    serv.hotkey('right')



copia()


opcao = serv.confirm('Escolha uma opção', buttons = ['Masculino', 'Feminino'])
if opcao == 'Masculino':
    x = 'masc'
else:
    x = 'femi'


espera_curta()
prox_pag()

aba_cadastro()

# Preenche campo CPF
cola()

espera_curta()
prox_campo()



# Preenche campo sexo
serv.write(x)
confirma()


for i in range(2):
    if not executando: break
    espera_curta()
    prox_campo()

prox_pag()

# Continua a execução verificando "executando" em cada passo
for execetundo in range (1):
    inicio_pag()
    serv.hotkey('right')

    # Preenche campo telefone
    copia()
    prox_pag()
    cola()

    prox_campo()
    for i in range(2):
        if not executando: exit()
        espera_curta()
        confirma()

    for i in range(2):
        if not executando: exit()
        espera_curta()
        prox_campo()

    prox_pag()

    if not executando: exit()
    inicio_pag()
    copia()
    espera_curta()
    prox_pag()
    cola()
    prox_campo()

    prox_pag()
    espera_curta()
    inicio_pag()

    for i in range(2):
        serv.hotkey('right')

    copia()
    prox_pag()
    espera_curta()
    cola()

    for i in range(2):
        espera_curta()
        prox_campo()

    prox_pag()
    espera_curta()
    inicio_pag()

    espera_curta()
    for i in range(5):
        serv.hotkey('right')

    if not executando: exit()
    copia()
    prox_pag()
    espera_curta()
    cola()

    prox_campo()
    serv.write(u) #email

    for i in range(2):
        prox_campo()

    prox_pag()

    espera_curta()
    serv.hotkey('left')
    copia()
    prox_pag()
    espera_curta()
    cola()
    prox_campo()
    serv.sleep(5)

    serv.write('00')

    espera_curta()
    for i in range(6):
        prox_campo()

    confirma()

    serv.sleep(5)
    for i in range(17):
        prox_campo()

    espera_curta()
    confirma()

#inicio do código para agendamento
    
    
    pag_anterior()
    serv.sleep(3)
    hora = serv.confirm('Escolha o Horário', buttons=['09:00', '18:00'])

    if not executando: exit()
    agendamento(hora)

#inicio do código para registrar atendimento
    
    if not executando: break
    atendimento()

    #registrar pagamento
    serv.sleep(2)
    pag = serv.confirm('Escolha a Forma de Pagamento', buttons=['Débito', 'Crédito', 'Pix', 'Dinheiro'])

    pagamento(pag)


    

print("Programa encerrado com sucesso!")



















