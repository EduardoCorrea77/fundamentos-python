def mostrar_primos(inicio, fim):
    for num in range(inicio, fim + 1):
        primo = True
        for i in range(2, num):
            if num % i == 0:
                primo = False
        if primo:
            print(num)

inicio = int(input("digite o início: "))
fim = int(input("digite o fim: "))
mostrar_primos(inicio, fim)
