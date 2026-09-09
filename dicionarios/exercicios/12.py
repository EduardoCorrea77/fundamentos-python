def remover():
    funcionario = {
        'nome': 'Eduardo',
        'idade': 16,
        'cargo': 'Programador',
        'salario': 3000,
        'telefone': '99999-9999'
    }
    print(funcionario)

    telefone = funcionario.pop('telefone')

    print(telefone)
    print(funcionario)

remover()