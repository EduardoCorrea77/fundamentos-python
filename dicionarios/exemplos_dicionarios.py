import json
def exibir_aluno():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16,
        'curso': 'Desenvolvimento de sistemas',
    }
    print('nome:',aluno['nome'])
    print('idade:',aluno['idade'])
    print('curso:',aluno['curso'])
    print('nota:',aluno.get('nota'))

#exibir_aluno()

def Atualizar_idade():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16,
        'curso': 'Desenvolvimento de sistemas',
    }
    print('idade antes:',aluno.get('idade'))
    aluno['idade'] = 18
    print('idade atual:',aluno.get('idade'))

#Atualizar_idade()

def adicionar_informacoes():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16,
    }
    print('aluno antes:',aluno)
    aluno['curso'] = 'Tecnico de eletro eletronica'
    aluno['nota'] = 9.3
    print('aluno atual:',aluno)

#adicionar_informacoes()

def verificar_chave():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16,
    }
    if 'nome' in aluno:
        print("o nome esta cadastrado")

    if 'nota' not in aluno:
        print("a nota não esta cadastrada")

#verificar_chave()

def verificar_aprovacao():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16,
        'nota': 8.5,
        'frequencia': 88
    }
    if aluno['nota'] > 6 and aluno['frequencia'] > 75:
        print(f"o aluno{aluno['nome']} esta aprovado")
    else:
        print(f"o aluno{aluno['nome']} esta reprovado")

#verificar_aprovacao()

def listar_campos():
    produto = {
        'nome': 'caneta azul',
        'quantidade': 50,
        'preco': 1.25
    }

    for chave in produto.keys():
        print(chave)

#listar_campos()

def listar_vaores():
    produto = {
    'nome': 'caneta azul',
    'quantidade': 50,
    'preco': 1.25
    }
    for valor in produto.values():
        print(valor)

#listar_vaores()

def exibir_produto():
    produto = {
        'nome': 'caneta azul',
        'quantidade': 50,
        'preco_unitario': 1.25
    }
    for chave, valor in produto.items():
        print(f'chave:{chave} possui o valor:{valor}')

#exibir_produto()

def atualizar_estoque():
    produto = {
        'nome': 'caneta azul',
        'quantidade': 67,
        'preco_unitario': 1
    }
    produto['total'] = produto['quantidade'] * produto['preco_unitario']
    print(produto)

#atualizar_estoque()

def remover_informacao():
    produto = {
        'nome': 'caneta azul',
        'quantidade': 67,
        'preco_unitario': 1
    }
    del produto['nome']

    preco_unitario = produto.pop('preco_unitario')
    print(produto, preco_unitario)

#remover_informacao()

def listar_produtos():
    produto = [
        {'nome': 'teclado ', 'preco': 299.00, 'quantidade': 2},
        {'nome': 'Mouse', 'preco': 25.00, 'quantidade': 3},
        {'nome': 'Monitor', 'preco': 1200.00, 'quantidade': 1}
    ]
    total_geral = 0
    for produto in produto:
        print(f'produto {produto["nome"]} custa {produto["preco"]}')
        total_idividual = produto['preco'] * produto['quantidade']
        total_geral += total_idividual

    print(f'o total geral é: {total_geral}')


#listar_produtos()

def cadastrar_aluno():
    aluno = {}

    aluno['nome'] = input('nome do aluno: ')
    aluno['idade'] = int(input('idade do aluno: '))
    aluno['curso'] = input('curso do aluno: ')
    aluno['email'] = input('email do aluno: ')

    print(f'dados cadastrados:{aluno}')

#cadastrar_aluno()

def criar_cadastro():
    quantidade = int(input('quantos dados voce deseja cadastrar: '))
    dados = {}

    for iten in range(quantidade):
        chave = input('informe uma chave: ')
        valor = input(f'informe um valor de {chave}: ')


        dados[chave] = valor

    print(iten + 1)
    print('cadastro final:', dados)

#criar_cadastro()

def calcular_media(notas):
    return sum(notas)/len(notas)


def aluno_completo():
    aluno = {
        'nome': 'Eduardo',
        'idade': 16,
        'curso': 'Desenvolvimento',
        'notas': [8.5, 6.0, 9.3, 8,2],
        'endereco': {
            'cidade': 'Piracicaba',
            'rua': 'Das Amoreiras',
            'numero': 1257,
            'telefone': '(19) 4420-6922'
        }
    }
    aluno['media'] = calcular_media(aluno['notas'])
    print(aluno[''][''])
#aluno_completo()

def cadastrar_dados_aluno():
    aluno = {}

    aluno['nome'] = input('nome do aluno: ')
    aluno['idade'] = int(input('idade do aluno: '))
    aluno['notas'] = []
    aluno['curso'] = input('curso do aluno: ')

    for nota in range(4):
        aluno['notas'].append(float(input(f"Digite a nota do aluno{nota + 1}:")))

    aluno['endereco'] = {}
    aluno['endereco']['cidade'] = input('cidade do aluno: ')
    aluno['endereco']['rua'] = input('rua do aluno: ')
    aluno['endereco']['numero'] = int(input('numero do aluno: '))
    aluno['endereco']['telefone'] = input('telefone do aluno: ')

    aluno['media'] = calcular_media(aluno['notas'])
    print("Aluno cadastrado", json.dumps(aluno, indent=4))

cadastrar_dados_aluno()