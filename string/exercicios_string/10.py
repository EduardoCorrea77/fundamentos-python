def separar_nome(nome_completo):
    partes_nome = nome_completo.split()
    return partes_nome

nome_completo = input("Digite seu nome completo: ")

partes = separar_nome(nome_completo)

for parte in partes:
    print(parte)