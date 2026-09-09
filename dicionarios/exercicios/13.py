def remover():
    funcionario = {
        'nome': 'Eduardo',
        'idade': 16,
        'cargo': 'Programador',
        'salario': 3000,
        'telefone': '99999-9999'
    }
    chave = input('Qual chave remover: ')

    if chave in funcionario:
        del funcionario[chave]

    print(funcionario)

remover()