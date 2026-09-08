def nome_maiusculo(nome):
    nome_maiusculo = nome.upper()
    return nome_maiusculo

nome = input("Digite seu nome: ")

print(f"Nome em maiúsculo: {nome_maiusculo(nome)}")