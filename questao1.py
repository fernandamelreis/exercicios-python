nome = input("Digite o seu nome:")
cpf = input("Digite o seu CPF: ")
idade = int(input("Digite a sua idade: "))
email = input("Digite o seu e-mail: ")
endereco = input("Digite o seu endereço: ")
nacionalidade = input("Digite a sua nacionalidade: ")

print("[1] OPÇÃO")
print("[2] OPÇÃO")

opcao = int(input("Digite uma opção: "))

if (opcao == 1):
    print("Confirme os dados: ")
    print("Nome: %s" %nome)
    print("CPF: %s" %cpf)
    print("Idade: %d" %idade)
    print("E-mail: %s" %email)
    
if (opcao == 2):
    print("Confirme os dados digitados...")
    print("Endereço: %s" %endereco)
    print("Nacionalidade: %s" %nacionalidade)