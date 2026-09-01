def calcular_media(notas):
    total = sum(notas)
    quantidade = len(notas)

    media = total / quantidade

    print(f"A média das notas é: {media}")
    return media
notas = [7.5, 8.0, 6.5, 9.0, 8.5]
calcular_media(notas)