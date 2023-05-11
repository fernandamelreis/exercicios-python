temperatura = int(input("Digite a temperatura atual em °C: "))

if (temperatura < 20):
    print("Está frio!")
else:
    if (temperatura == 20):
        print("Temperatura ambiente!")
    else:
        print("Está calor!")