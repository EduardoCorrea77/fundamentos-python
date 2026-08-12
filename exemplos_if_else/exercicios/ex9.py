def calculadora():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, * ou /): ")

    if operacao == "+":
        print(numero1 + numero2)
    elif operacao == "-":
        print(numero1 - numero2)
    elif operacao == "*":
        print(numero1 * numero2)
    elif operacao == "/":
        if numero2 == 0:
            print("não é possível dividir por zero")
        else:
            print(numero1 / numero2)
    else:
        print("Operação inválida")

calculadora()