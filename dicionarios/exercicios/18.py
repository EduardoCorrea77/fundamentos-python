produtos = []


def cadastrar():
    produto = {}

    produto['nome'] = input('Nome: ')
    produto['preco'] = float(input('Preço: '))
    produto['estoque'] = int(input('Estoque: '))

    produtos.append(produto)

def listar():
    for produto in produtos:
        print(produto)

def buscar():
    nome = input('Nome do produto: ')

    for produto in produtos:
        if produto['nome'] == nome:
            print(produto)

def atualizar():
    nome = input('Nome do produto: ')

    for produto in produtos:
        if produto['nome'] == nome:
            quantidade = int(input('Quantidade: '))
            produto['estoque'] += quantidade

def remover():
    nome = input('Nome do produto: ')

    for produto in produtos:
        if produto['nome'] == nome:
            produtos.remove(produto)

while True:
    print('1 - Cadastrar')
    print('2 - Listar')
    print('3 - Buscar')
    print('4 - Estoque')
    print('5 - Remover')
    print('6 - Sair')

    opcao = input('Escolha: ')
    if opcao == '1':
        cadastrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        buscar()
    elif opcao == '4':
        atualizar()
    elif opcao == '5':
        remover()
    elif opcao == '6':
        break
    else:
        print('Opção inválida')