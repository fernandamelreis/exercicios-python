print("[1] CADASTRO")
print("[2] AUTENTICAÇÃO")
print("[3] SAIR")


opcao = int(input("Digite uma opção: "))

if opcao == 1:
    print("---REGISTER ----")

    nome = input("Digite o seu nome completo: ") #string
    idade = int(input("Digite a sua idade: "))
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")
    cpf = input("Digite o seu CPF: ")


    print("Nome: %s" %nome)
    print("Idade: %d" %idade)
    print("E-mail: %s" %email)
    print("Senha: %s" %senha)
    print("CPF: %s" %cpf)
    print("Successfully registered user!")

elif opcao == 2:
    
    print("---AUTENTICATION---")
    email = input("Digite o seu e-mail: ")
    password = input("Digite a sua senha: ")
    
    email_admin = "admin@email.com"
    password_admin = "123456"
    
    print("--------------------")
    print("E-mail: %s" %email)
    print("Senha: *******")
    
    if (email_admin == email) and (password_admin == password):
        print("Successyfully authenticated user!")
    else:
        print("Dados incorretos. Tente novamente!")

elif opcao ==3:
    
    print("LOGOFF...")
    print("Responda Y para SIM e N para NÃO")
    resp = input("Deseja realmente sair do sistema? ___")

    if resp == "Y":
        print("Usuário está sendo deslogado do sistema...")
    else:
        print("Usuário continua conectado no sistema...")

else:
    print("Opção inválida escolha 1, 2 ou 3!")

