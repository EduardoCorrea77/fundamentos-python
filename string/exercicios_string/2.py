def nome_minusculo(nome):
    nome_minusculo = nome.lower()
    return nome_minusculo

nome = input("Digite seu nome: ")

print(f"Nome em minúsculo: {nome_minusculo(nome)}")