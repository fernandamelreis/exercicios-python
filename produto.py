
print("[1]. PRODUTO DE HIGIENE PESSOAL")
print("[2]. PRODUTO DE LIMPEZA")
print("[3]. PRODUTO DE GENERO ALIMENTICIO")


produto = int(input("Digite uma opcao: "))


if produto == 1:
    print("Produto da categoria de higiene pessoal")
elif produto == 2:
    print("Produto da categoria de limpeza")
elif produto == 3:
    print("Produto categoria genero alimenticio")
else:
    print("Produto nao localizado!")
