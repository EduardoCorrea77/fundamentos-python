def mostrar_inpares():
    numero = int(input("Digite um numero inteiro maior que 1: "))
    for i in range(0, numero + 1):
        if i % 2 == 1:
            print(i)
mostrar_inpares()
