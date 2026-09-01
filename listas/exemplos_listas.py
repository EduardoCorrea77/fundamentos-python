def mostrar_nomes(nomes):
    for nome in nomes:
        print(f"O nome da lista é: {nome}")


lista_de_nomes = ["Renan", "Moises", "Rafael", "Ana", "Clayton"]
mostrar_nomes(lista_de_nomes)

# Adicionando novo nome na lista
def adicionar_nome(nomes, nome):
    nomes.append(nome)
    print(nomes)

adicionar_nome(lista_de_nomes, "Isabela")


# Adicionando novo nome em uma posição especifica
def adicionar_nome_posicao(nomes, nome, posicao):
    nomes.insert(posicao, nome)
    print(f"O nome {nome} foi inserido na posição {posicao} de lista: {nomes}")

adicionar_nome_posicao(lista_de_nomes, "Rogerio", 2)

# Juntando duas listas
def juntar_nomes(nomes, novos_nomes):
    nomes.extend(novos_nomes)
    print(f"Os novos nomes {novos_nomes} foram inseridos na lista {nomes}")


novos_nomes = ["Francisco", "Marcio"]
juntar_nomes(lista_de_nomes, novos_nomes)


# Removendo itens da lista
def remover_nome_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Este nome não existe na lista")
    else:
        nomes.remove(nome)
        print(f"O nome {nome} foi removido na lista {nomes}")

remover_nome_pelo_valor(lista_de_nomes, "Francisco")

# Removendo nome pelo indice
def remover_nome_pelo_indice(nomes, posicao):
    nomes.pop(posicao)
    print(f"O nome da posição {posicao} é {nomes[posicao]} foi, removido")

remover_nome_pelo_indice(lista_de_nomes, 4)

# Descobrindo posição pelo nome
def encontrar_posicao_pelo_valor(nomes, nome):
    if nome not in nomes:
        print("Nome não emcontrado")
    else:
        posicao = nome.index(nome)
        print(f"A posição do nome {nome} é {posicao}")

encontrar_posicao_pelo_valor(lista_de_nomes, "Moises")

# Contando elementos da lista
def quantidade_de_nomes(nomes):
    quantidade = len(nomes)
    print(f"Quantidade de nomes da lista {quantidade}")

quantidade_de_nomes(lista_de_nomes)

# Ordenando os elementos da lista
def ordenar_nomes(nomes):
    lista_de_nomes_ordenados = sorted(nomes)
    print(f"A lista ordenada é´{lista_de_nomes_ordenados}")

ordenar_nomes(lista_de_nomes)

# Operações matematicas
# Calcular media
def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)
    media = total / quantidade
    print(f"A media das notas é {media}")

notas_semestre = [7.8, 6.5, 9, 8.7, 9.5]
calcular_media(notas_semestre)

def gerenciar_notas(notas, nova_nota):
    notas.append(nova_nota)
    ordenadas = sorted(notas)

    media = sum(notas) / len(notas)

    return ordenadas, media

notas_ordenadas, media = gerenciar_notas(notas_semestre, 6.7)
print(f"notas ordenadas = {notas_ordenadas}")
print(f"A media das notas é {media}")

def adicionar_produto(produtos, produto):
    produtos.append(produto)
    print(f"Minha lista de produtos: {produtos}")

lista_produtos = [
    ["Arroz", 2, 32.00],
    ["Feijão", 3, 8.50]
]

novo_produto = ["Café", 2, 28.00]
adicionar_produto(lista_produtos, novo_produto)

def quantidade_total_produtos(produtos):
    quantidade = []

    for produto in produtos:
        quantidade.append(produto[1])

    return sum(quantidade)

quantidade_produtos = quantidade_total_produtos(lista_produtos)
print(f"Quantidade total de produtos: {quantidade_produtos}")

def valor_total_produtos(produtos):
    valores = []

    for produto in produtos:
        valor = produto[1] * produto[2]
        valores.append(valor)

    return sum(valores)

preco_total_produtos = valor_total_produtos(lista_produtos)
print(f"valor total de produtos: {preco_total_produtos}")