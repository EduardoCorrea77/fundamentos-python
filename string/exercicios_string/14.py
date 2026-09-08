def validar_telefone(numeros):
    telefone_valido = numeros.isdigit()

    if telefone_valido:
        print("Número de telefone válido!")
    else:
        print("Número inválido! Digite somente números.")

numeros = input("Digite seu telefone: ")

validar_telefone(numeros)