nota1 = float(input("Digite a 1o. nota: "))
nota2 = float(input("Digite a 2o. nota: "))
nota3 = float(input("Digite a 3o. nota: "))
nota4 = float(input("Digite a 4o. nota: "))
media = float


media = (nota1 + nota2 +nota3 + nota4)/4

print("A média é: %6.2f" %media)

if (media >= 6):
    print("Aprovado!")
else:
    print("Reprovado!")