def validar_senha(senha):
    contem_letra = False
    contem_numero = False
    contem_espaco = False

    for caractere in senha:
        if caractere.isalpha():
            contem_letra = True

        if caractere.isdigit():
            contem_numero = True

        if caractere.isspace():
            contem_espaco = True

    tamanho_valido = len(senha) >= 8

    if tamanho_valido and contem_letra and contem_numero and not contem_espaco:
        print("Senha válida!")
    else:
        print("Senha inválida!")

senha = input("Digite sua senha: ")

validar_senha(senha)