print("[1] CADASTRO")
print("[2] LOGIN")
print("---------------------")


opcao = int(input("Digite uma opção: "))

if (opcao == 1):
    print("Realizando cadastro...")
    nome = input("Digite o seu nome: ")
    email = input("Digite um e-mail: ")
    senha = input("Digite uma senha: ")
    
    print("---------------------")
    print("Lendo informações...")
    print("Nome: %s" %nome)
    print("E-mail: %s" %email)
    print("Senha: %s" %senha)
    print("Usuário cadastrado!")
    
if (opcao == 2):
    
    print("Realizando o login...")
    email = input("Digite um e-mail: ")
    senha = input("Digite uma senha: ")
    
    print("---------------------")
    print("Lendo informações...")
    print("E-mail: %s" %email)
    print("Senha: %s" %senha)
    print("Usuário autenticado!")