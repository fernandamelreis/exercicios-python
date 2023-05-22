num1 = int(input("Digite o 1o. número: "))
num2 = int(input("Digite o 2o. número: "))

opcao = int(input("Digite uma opção: "))

if opcao == 1:
    
    media = float
    media = (num1+ num2)/2
    print("A média é: %6.2f" %media)
    
elif opcao == 2:
    
    sub = int
    if (num1 > num2):
        sub = num1 - num2
        print("A subtração é: %d" %sub)
    else:
        sub = num2 = num1
        print("A subtração é: %d" %sub)
elif opcao == 3:
    
    mult = int
    mult = num1 * num2
    print("A multiplicação é: %d" %mult)
elif opcao == 4:
    divisao = float
    if (num2 != 0 ):
        divisao = num1 / num2
        print("A divisão é: %6.2f" %divisao)
    else:
        print("Não é possível fazer a divisão!")
else: 
    print("Opção inválida! Digite 1, 2, 3 ou 4.")