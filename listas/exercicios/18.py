def analisar_temperaturas(temperaturas):
    quantidade = len(temperaturas)

    soma = sum(temperaturas)
    media = soma / quantidade
    temperaturas_ordenadas = sorted(temperaturas)

    print(f"Quantidade de temperaturas: {quantidade}")
    print(f"Soma das temperaturas: {soma}")
    print(f"Média das temperaturas: {media}")
    print(f"Temperaturas ordenadas: {temperaturas_ordenadas}")

    return quantidade, soma, media, temperaturas_ordenadas
temperaturas = [28, 32, 25, 30, 27]

analisar_temperaturas(temperaturas)