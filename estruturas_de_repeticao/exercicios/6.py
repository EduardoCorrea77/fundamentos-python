def somar_ate():
    numero = int(input("Digite um número: "))
    soma = 0

    for i in range(1, numero + 1):
        soma += i

    return soma


resultado = somar_ate()

print("A soma é:", resultado)