salario = float(input("Digite o seu salário: "))

if (salario < 500):
    reajuste = float
    
    reajuste = salario + (salario * 0.3)
    print("O salário reajustado é: %6.2f" %reajuste)
else:
    print("Você não tem direito ao reajuste!")
