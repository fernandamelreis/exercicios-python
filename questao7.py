funcionarios = ['Nome: Miguel', 'CPF: 111.111.111-11', 'Cargo: ANALISTA JR', 'Salário: 3276.30', 
                'Nome: Romário', 'CPF: 222.222.222-22', 'Cargo: GERENTE DE PROJETO', 'Salário: 6478.20',
                'Nome: Priscila', 'CPF: 444.444.444-44', 'Cargo: ANALISTA JR', 'Salário: 3276.30',
                'Nome: Jorge', 'CPF: 333.333.333-33', 'Cargo: ANALISTA JR', 'Salário: 3276.30']

contador = 0

for funcionario in funcionarios:
    print(funcionario)
    contador = contador + 1
    print(contador)
    
    if (funcionario == 'Nome: Priscila '):
        print("Nome Priscila encontrado! Encerrando o loop...")
        break