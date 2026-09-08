def separar_dados():
    dados = "Eduardo,16,Estudante,Piracicaba"

    dados_separados = dados.split(",")

    nome = dados_separados[0]
    idade = dados_separados[1]
    profissao = dados_separados[2]
    cidade = dados_separados[3]

    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Profissão: {profissao}")
    print(f"Cidade: {cidade}")

separar_dados()