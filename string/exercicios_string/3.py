def formatar_nome(nome):
    nome_formatado = nome.title()
    return nome_formatado

nome = input("Digite seu nome completo: ")

print(f"Nome formatado: {formatar_nome(nome)}")