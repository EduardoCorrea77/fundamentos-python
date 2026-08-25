def fatorial(numero):
    if numero < 0:
        return "Não existe fatorial de número negativo."

    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

numero = int(input("digite um número: "))
print(fatorial(numero))
fatorial(numero)

