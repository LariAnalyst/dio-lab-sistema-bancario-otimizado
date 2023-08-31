import textwrap
#import textwrap = organizar blocos de texto em parágrafos ou linhas de largura fixa
#Sitema Bancário Lari Analyst 
#Objetivo geral: Separar as funções de saque, depósito e extrato em funções. 
#Criar duas novas funções: cadastrar usuário (cliente) e cadastrar conta bancária.

menu_inicio = (f"""
    Seja bem-vindo ao Banco Lari Analyst 
    Escolha qual operação deseja realizar:
    [1] Sacar 
    [2] Depositar 
    [3] Visualizar Extrato 
    [4] Nova conta 
    [5] Listar contas
    [6] Novo usuário           
    [7] Sair         
    """)

#print(menu_inicio)
print(textwrap.dedent(menu_inicio))

def saque (*, saldo, valor, extrato, limite, numero_saque, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = numero_saque >= limite_saques

    if excedeu_saldo:
        print('Saldo insuficiente')

    elif excedeu_limite:
        print('O seu limite de saque é de 500 reais, refaça a operação')

    elif excedeu_saque:
        print('Você ultrapassou o seu limite de saque, você pode fazer 3 operações de saque por dia')
                
    elif valor > 0: 
        saldo = saldo - valor
        extrato += f"Saque: R$ {valor:.2f}\n "
        numero_saque = numero_saque + 1
        print("\nSaque realizado com sucesso!")
        
    else:
        print("Operação falhou, valor negativo")

    return saldo, extrato

def deposito (saldo, valor, extrato, /):
    if valor > 0:
        saldo = valor + saldo
        extrato += f"Deposito: R$ {valor:.2f}\n "
        print("\nDepósito realizado!")
    else:
        print("Valor negativo, não é possível depositar")
    
    return saldo, extrato

def exibir_extrato (saldo, *, extrato):
    print("--------------------------")
    print("         Extrato          ")
    print("--------------------------")
    print("Não foram realizadas operações." if not extrato else extrato)
    print(f"\n Saldo: R$:{saldo:.2f}")
    print("--------------------------")

def nova_conta (agencia, numero_conta, usuarios):
    CPF = input("Digite o CPF: Somente números ")
    usuario = filtrar_usuario(CPF, usuarios)

    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
        
    print("\nUsuário não encontrado, fluxo de criação de conta finalizado!")
        
def listar_contas (contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome_usuario']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))
        #textwrap.dedent(text): Remove a indentação comum a todas as linhas de um bloco de texto. 
        #Isso é útil quando você tem um texto multilinha com indentação e deseja remover essa indentação. 

def novo_usuario (usuarios):
    CPF = input("Digite o CPF: Somente números ")
    usuario = filtrar_usuario(CPF, usuarios)

    if usuario:
        print("Esse usuário já está cadastrado")
        return
    
    nome_usuario = str(input("Digite o nome do novo usuário: "))
    data_de_nascimento = input("Digite a data de nascimento no formado dd/mm/aaaa: ")
    endereco_usuario = input("Digite o endereço no formato: Logradouro, número - bairro - cidade/sigla estado: ")
    
    usuarios.append({"nome_usuario":nome_usuario, "data_de_nascimento":data_de_nascimento, "CPF":CPF, "endereco_usuario":endereco_usuario})

    print("Usuário criado com sucesso!")

def filtrar_usuario (CPF, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["CPF"] == CPF]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    escolha_menu = -1
    saldo = 0
    limite = 500
    extrato = ""
    numero_saque = 0
    usuarios = []
    contas = []
    
    while escolha_menu  != 0:
        escolha_menu = int(input("Digite o número da operação escolhida: "))

        if escolha_menu == 1:
            valor = float(input("Você escolheu saque, digite quanto deseja sacar: \n"))

            saldo, extrato = saque (
                saldo=saldo, 
                valor=valor, 
                extrato=extrato,
                limite=limite,
                numero_saque=numero_saque,
                limite_saques=LIMITE_SAQUES,
            )
        
        elif escolha_menu == 2:
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = deposito(saldo, valor, extrato)

        elif escolha_menu == 3:
            exibir_extrato (saldo, extrato=extrato)

        elif escolha_menu == 4:
            numero_conta = len(contas) + 1
            conta = nova_conta (AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif escolha_menu == 5:
            listar_contas (contas)  

        elif escolha_menu == 6:
            novo_usuario (usuarios)   

        elif escolha_menu == 7:
            print("\nVocê escolheu sair, Obrigada por usar o nosso banco!")
            break

        else: 
            print("Opção inválida")

main()