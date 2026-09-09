def consultar():
    cliente = {
        'nome': 'Eduardo',
        'idade': 16,
        'cidade': 'Piracicaba'
    }
    chave = input('Digite a informação: ')

    resultado = cliente.get(chave)

    if resultado:
        print(resultado)
    else:
        print('Informação não encontrada.')

consultar()