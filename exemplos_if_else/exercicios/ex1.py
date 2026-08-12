def numero_inteiro():
    numero = int(input("Digite um numero inteiro: "))
    if numero > 0:
        print(f"o numero {numero} é positivo")
    elif numero < 0:
        print(f"o numero {numero} é negativo")
    else:
        print(f"o numero {numero} é igual a zero")
numero_inteiro()