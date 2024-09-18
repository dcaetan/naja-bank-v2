import textwrap

def menu():
    menu = """
    =============== Menu ============

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova Conta
    [5] Listar Contas
    [6] Novo Usuario
    [0] Sair

    ============ Naja Bank ==========

    Digite a opção desejada: """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R${valor:.2f}\n"
    else:
        print("\nOps! O valor informado é inválido.")
            
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
     
    excedeu_valor_saldo = valor > saldo
    excedeu_valor_limite = valor > limite
    excedeu_valor_saques = numero_saques >= limite_saques

    if excedeu_valor_saldo:
        print("\nOps! Saldo insuficiente.")
    elif excedeu_valor_limite:
        print("\nOps! Saque excedeu o limite.")
    elif excedeu_valor_saques:
        print("\nOps! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor:.2f}\n"
        numero_saques += 1
    else:
        print("\nOps! O valor informado é inválido.")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    
    print("\n---------------- Info. Extrato ----------------")
    print("Não foram realizadas transações.\n" if not extrato else extrato)
    print(f"Saldo: R${saldo:.2f}")
    print("-----------------------------------------------")

def criar_usuario(usuarios): # [6] Novo Usuário

    cpf = input("Digite seu CPF (Apenas números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\nOps! Usuário já cadastrado.")
        return
    
    nome = input("Digite seu Nome Completo: ")
    data_nascimento = input("Digite sua Data de Nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu endereço (Rua, N°, Complemento (Apto.), Bairro - Cidade/UF): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("\nUsuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):

    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios): # [4] Nova Conta

    cpf = input("\nDigite seu CPF (Apenas Números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criado com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\nOps! Usuário não encontrado.")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Ag: {conta['agencia']}
            C/c: {conta['numero_conta']}
            Titular: {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 3

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1": # [1] Depositar

            valor = float(input("\nInforme o valor do Déposito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2": # [2] Sacar

            valor = float(input("\nInforme o valor do Saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "3": # [3] Extrato

            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4": # [4] Nova Conta
            
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_saques, usuarios)

            if conta:
                contas.append(conta)
        
        elif opcao == "5": # [5] Listar Contas

            listar_contas(contas)

        elif opcao == "6": # [6] Novo Usuario

            criar_usuario(usuarios)

        elif opcao == "0": # [0] Sair
            print("\nObrigado por utilizar o Naja Bank\n")
            break
        else:
            print("\nOperação inválida, digite novamente a opção desejada.")

main()