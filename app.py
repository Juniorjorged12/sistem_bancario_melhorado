menu = """
    Bem vindo ao seu sistema bancário,
    escolha uma opção abaixo para prosseguir!!!!
    
                [d] Depositar
                [s] Sacar
                [e] Extrato
                [cu]Cadastrar Usuario
                [cc]Cadastrar Conta
                [q] Sair
>>>
"""

saldo = 0
limite = 500
LIMITE_SAQUES = 3
quant_saque = 0


lista_deposito = []
lista_saque = []

cpf = []
nomes = []
usuario = []
conta = []

def deposito():
    """
    função responsavel por realizar a operação de deposito do usuario
    :return:  o saldo, e adiciona o valor na lista de deposito
    """

    valor = float(input("Valor do deposito R$: "))
    if valor > 0:
        global saldo
        saldo += valor
        lista_deposito.append(valor)
        print(f'O valor de R${valor:.2f}, foi depositado com sucesso na sua conta')

    else:
        print("Insira o valor correto para depósito")


def saque():
    """
    função por realizar o saque na conta do usuario
    :return: saldo, e adiciona o valor na lista de saques
    """

    saque = float(input("Insira o valor a ser sacado R$: "))
    global saldo, quant_saque
    if quant_saque == LIMITE_SAQUES:
        print("Voce atingiu seu limite de saque diário")

    elif saque < limite and saque < saldo:

        saldo -= saque
        quant_saque += 1
        lista_saque.append(saque)
        print(f"O valor de R${saque:.2f}, foi sacado com sucesso de sua conta")
        return saldo
    else:
        print("Voce nao tem limite ou o valor do saque excedeu o maximo permitido pela agencia!!!")


def extrato():
    """
    percorre as listas de deposito e de saque exibindo todos os itens dela  e exibe o saldo tambem
    :return: lista de deposito, lista de saque e saldo
    """
    for itens in lista_deposito:
        print(f"Voce realizou um deposito de R$:{itens:.2f}")
    for itens in lista_saque:
        print(f"Voce realizou um saque no valor de R$:{itens:.2f}")
    print(f"Seu saldo é de {saldo:.2f}")

def cadastro_usuarios():
    num = input('Digite os numeros do CPF do Usuário : ')
    while num in cpf:
        num = input('CPF digitado ja está cadastrado digite um novo numero de  cpf: ')
    cpf.append(num)
    nome = input('Nome completo do usuário: ')
    nomes.append(nome)
    nasc = input('Data de nascimento (dd-mm-aaaa):  ')
    endereco = input('Informe endereço completo do cliente (logradouro, nro - bairro - cidade/est): ')
    usuario.append({'nome':nome, 'data_de_nascimento': nasc, 'cpf':num, 'endereço': endereco })

    print('Usuario cadastrado com sucesso')

def criar_conta():

    num = input('Informe o CPF do usuario cadastrado:')
    if num in cpf :
        num_agencia = input('Numero da agencia: ')
        num_conta = input('Numero da conta: ')
        posicao = cpf.index(num)
        nome = nomes[posicao]

        conta.append({'Nome':nome, 'Agencia':num_agencia, 'Conta':num_conta})
    else:
        print('O CPF digitado nao corresponde ao de um Usuário cadastrado')












while True:
    opcao = input(menu)
    if opcao == "d":
        deposito()


    elif opcao == "s":
        saque()


    elif opcao == "e":
        extrato()

    elif opcao == "cu":
        cadastro_usuarios()

    elif opcao =="cc":
        criar_conta()


    elif opcao == "q":
        break
    else:
        print('Digite uma opção válida')




