num1 = int(input("Digite o 1o. número: "))
num2 = int(input("Digite o 2o. número: "))

soma = num1 + num2

print("Soma: %d", soma)

if (soma%2 == 0):
    print("A soma é par! ")
else:
    print("A soma é impar! ")