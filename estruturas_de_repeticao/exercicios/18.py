def caixa_eletronico(valor):
    notas = [100, 50, 20, 10, 5, 2]

    for nota in notas:
        quantidade = 0

        while valor >= nota:
            valor -= nota
            quantidade += 1

        if quantidade > 0:
            print(quantidade, "nota(s) de", nota)


valor = int(input("Digite o valor do saque: "))

caixa_eletronico(valor)