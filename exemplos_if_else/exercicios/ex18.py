def frete():
    compra = float(input("Digite o valor da compra: R$ "))

    if compra <= 100:
        valor_frete = 20
    elif compra <= 300:
        valor_frete = 10
    else:
        valor_frete = 0

    total = compra + valor_frete

    print(f"Frete: R$ {valor_frete:.2f}")
    print(f"Valor total: R$ {total:.2f}")


frete()