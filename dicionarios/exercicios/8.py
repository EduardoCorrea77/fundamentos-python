def login():
    usuario = {
        'login': 'Eduardo',
        'senha': '1234'
    }

    login = input('Login: ')
    senha = input('Senha: ')

    if login == usuario['login'] and senha == usuario['senha']:
        print('Entrou')
    else:
        print('Login ou senha errados')

login()