def desconto():
    valor = float(input("Digite o valor da compra: "))

    if valor <= 100:
        desconto = 0
    elif valor <= 500:
        desconto = 0.10
    else:
        desconto = 0.15

    valor_desconto = valor * desconto
    valor_final = valor - valor_desconto

    print(f"Desconto: R$ {valor_desconto}")
    print(f"Valor final: R$ {valor_final}")


desconto()