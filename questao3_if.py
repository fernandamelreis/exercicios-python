print("[1] CADASTRO ALUNO")
print("[2] IMPRIMIR DADOS")
print("[3] CALCULAR MÉDIA")
print("[4] IMPRIMIR BOLETIM")


opcao = int(input("Digite uma opção: "))

if (opcao == 1):
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = input("Digite o cpf do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    
    print("--------------------")
    print("Aluno cadastrado!")
    print("--------------------")
    
elif (opcao == 2):
    
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = input("Digite o cpf do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    
    print("-----------------------------")
    print("--IMPRIMINDO DADOS DO ALUNO--")
    print("Nome: %s" %nome)
    print("Idade: %d" %idade)
    print("CPF: %s" %cpf)
    print("E-mail: %s" %email)
    print("Aluno cadastrado!")
    print("-----------------------------")
    

elif (opcao == 3):
    
    nota1 = float(input("Digite a 1o. nota: "))
    nota2 = float(input("Digite a 2o. nota: "))
    nota3 = float(input("Digite a 3o. nota: "))
    nota4 = float(input("Digite a 4o. nota: "))
    
    media = float
    media = (nota1+nota2+nota3+nota4)/4
    
    print("A média é: %6.2f" %media)
    
    if(media >=6):
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")
elif (opcao == 4):
    
    nome = input("Digite o nome do aluno: ")
    idade = int(input("Digite a idade do aluno: "))
    cpf = input("Digite o cpf do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    
    nota1 = float(input("Digite a 1o. nota: "))
    nota2 = float(input("Digite a 2o. nota: "))
    nota3 = float(input("Digite a 3o. nota: "))
    nota4 = float(input("Digite a 4o. nota: "))
    
    media = float
    media = (nota1+nota2+nota3+nota4)/4
    
    print("A média é: %6.2f" %media)
    
    print("-----------------------------")
    print("------BOLETIM DO ALUNO-------")
    print("Nome: %s" %nome)
    print("Idade: %d" %idade)
    print("CPF: %s" %cpf)
    print("E-mail: %s" %email)
    print("1o. nota: %6.2f" %nota1)
    print("2o. nota: %6.2f" %nota2)
    print("3o. nota: %6.2f" %nota3)
    print("4o. nota: %6.2f" %nota4)
    print("Média: %6.2f" %media)
    print("-----------------------------")
    
    if(media >=6):
        print("Situação do aluno:")
        print("Aluno aprovado!")
    else:
        print("Situação do aluno:")
        print("Aluno reprovado!")
    
    
else: 
    
    print("Digite uma opção válida!")
