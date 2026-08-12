def numero():
    numero1 = int(input("digite o primeiro numero: "))
    numero2 = int(input("digite o segundo numero: "))
    if numero1 > numero2:
        print(f"o primeiro numero e maior que o segundo")
    elif numero1 < numero2:
        print(f"o segundo numero e maior que o primeiro")
    elif numero1 == numero2:
        print(f"os numeros sao iguais")
numero()
