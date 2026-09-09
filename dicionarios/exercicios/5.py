def cadastro():
    dados = {}
    quantidade = int(input('Quantos dados: '))

    for i in range(quantidade):
        chave = input('Chave: ')
        valor = input('Valor: ')

        dados[chave] = valor
    print(dados)

cadastro()