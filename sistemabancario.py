#Sistema Bancario

#Importações

import datetime
import os

#Variaveis Globais
menu = """


-------------------------------------------
[            BANCO REAL DO SUL            ]
-------------------------------------------
Escolha a operação desejada:
-------------------------------------------
[1] Depositar             [2] Sacar
[3] Extrato               [9] Sair
-------------------------------------------


"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
sair_extrato = 0

#Constantes
LIMITE_SAQUE_DIARIO = 3

#Funções:

#Função limpa tela

def limpa_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função Deposito

def deposito (valor_d):
    global saldo, extrato
    if valor_d >= 0:
        saldo = saldo + valor_d
        print (f"Depósito de R$ {valor_d:.2f} efetuado.")
        data_hora = (datetime.datetime.now()).strftime("%d/%m/%Y %H:%M:%S") #Pega a data e hora atual e formata como DD/MM/AAAA HH:MM:SS
        extrato = extrato + f"""
        ---------------------------------------------------------
         - OPE-001 Deposito de R$ {valor_d:.2f} - {data_hora}
        """
    else:
        print ("Valores negativos não são permitidos em depositos.")

#Função Saque

def saque (valor_s):
    global saldo, LIMITE_SAQUE_DIARIO, numero_saques, extrato
    if numero_saques < LIMITE_SAQUE_DIARIO:
        if valor_s <= 500 and valor_s > 0:
            if valor_s < saldo:
                saldo -= valor_s
                numero_saques += 1
                print (f"Saque de R$ {valor_s:.2f} efetuado.")
                data_hora = (datetime.datetime.now()).strftime("%d/%m/%Y %H:%M:%S") #Pega a data e hora atual e formata como DD/MM/AAAA HH:MM:SS
                extrato = extrato + f"""
        ---------------------------------------------------------
         - OPE-002 Saque de R$ {valor_s:.2f} - {data_hora}
        """
                return True
            else:
                print ("Saldo insuficiente.")
                return False
        else:
            print ("Valor não permitido.")  
            return False    
    else:
        print ("Quantidade de saques excedido.")
        return False

#Função Extrato

def extrato_v (solicita_e):
    print ("Nada definido.")

#Inicio do programa

while True:

    opcao = input (menu)
    limpa_tela()
    if opcao == "1":  
        valor_d = float(input("Informe o valor de depósito: "))
        deposito(valor_d)
    elif opcao == "2":
        valor_s = float(input("Informe o valor de saque: "))
        saque(valor_s)
    elif opcao == "3":
        print ("""
        [                    INÍCIO DO EXTRATO                    ]
        """)
        print (f"{extrato}")
        print (f"""
                  SALDO ATUAL: R$ {saldo:.2f}
        """)
        print ("""
        [                     FIM DO EXTRATO                      ]
        """)
    elif opcao == "9":
        break
    else:
        print ("Opção inválida!")
print ("Obrigado por ser nosso cliente.")















