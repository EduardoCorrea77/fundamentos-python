def calcular_media():
    soma = 0
    quantidade = 0
    while True:
        numero = int(input("Digite um número: "))
        if numero == 0:
            break
        soma += numero
        quantidade += 1
    return soma / quantidade

print(calcular_media())
