def criar_email(nome, sobrenome, dominio):
    nome_minusculo = nome.lower()
    sobrenome_minusculo = sobrenome.lower()

    email = nome_minusculo + "." + sobrenome_minusculo + "@" + dominio

    return email

nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
dominio = input("Digite o domínio: ")

print(f"E-mail: {criar_email(nome, sobrenome, dominio)}")