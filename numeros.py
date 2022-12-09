print("Categorias...")
print("ESCOLHA UMA OPCAO:")
print("[1] Alimentos")
print("[2] Congelados")
print("[3] Higiene Pessoal")
print("[4] Hortalicas")

categoria = int(input("Digite a categoria do produto: "))


if categoria == 1:
    preco = 10
    print("O produto eh de genero alimenticio, o seu preco eh: ", preco)
elif categoria == 2:
    preco = 20
    print("O produto eh de genero Congelados, o seu preco eh: ", preco)
elif categoria == 3:
    preco = 30
    print("O produto eh do genero de higiene pessoal, o seu preco eh: ", preco)

elif categoria == 4:
    preco = 40
    print("O produto eh do genero de hortalicas, o seu preco eh: ", preco)
else:
    print("Categoria inválida, digite um valor entre 1 a 4!")
    preco = 0
    print("O preço do produto é: R$%6.2f" % preco)
