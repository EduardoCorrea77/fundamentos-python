def mostrar_pares():
    numero = int(input("Digite um numero inteiro maior que 1: "))
    for i in range (0, numero + 1):
        if i % 2 == 0:
            print(i)
mostrar_pares()