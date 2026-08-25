def eh_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

numero = int(input("digite um número: "))
print(eh_primo(numero))
