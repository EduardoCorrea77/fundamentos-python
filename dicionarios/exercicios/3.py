def adicionar():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16
    }
    aluno['email'] = input('Email: ')
    aluno['endereco'] = input('Endereço: ')
    aluno['telefone'] = input('Telefone: ')

    print(aluno)

adicionar()