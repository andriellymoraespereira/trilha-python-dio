from resolução_desafio2 import filtrar_usuario


def menu():
    menu = """
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [c] Cadastrar usuário
    [cc] Cadastrar Conta
    [q] Sair

    => """
    return input(menu)


def Depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! Valor inválido")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_saque = numero_saques >= limite_saques
    excedeu_limite = valor > limite

    if excedeu_saldo:
        print("Saldo Insuficiente!")

    elif excedeu_saque:
        print("Você excedeu seu limite de saque diário!")

    elif excedeu_limite:
        print("Valor de saque excede o limite!")    

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"        
        numero_saques += 1
        print("Saque realizado com sucesso!")

    else:
        print("Operação falhou! O valor informado é invalido")    

    return saldo, extrato   


def extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO =================")
    print("Não forem realizados movimentacões" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("==========================================")


def cadastrar_usuario():
    usuario = []
    cpf = input("Informe o CPF": )
    nome = input("Informe seu nome: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuario.append({"nome" : nome ,"cpf":cpf, "data_nascimento": data_nascimento, "endereco":endereco })
    print("Usuário criado com sucesso!")
   
def criar_conta(AGENCIA, numero_conta, usuario):
    AGENCIA = '000,1'
    numero_conta += 1
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf)
    print("Conta criada com sucesso!")
    
    return {"AGENCIA": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
   

