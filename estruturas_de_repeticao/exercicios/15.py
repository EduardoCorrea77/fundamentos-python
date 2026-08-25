def maior_numero():
    maior = 0
    continuar = "s"
    while continuar == "s":
        numero = int(input("Digite um número: "))
        if numero > maior:
            maior = numero
        continuar = input("Deseja continuar? (s/n): ")
    return maior

print(maior_numero())
