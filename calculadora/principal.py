from calculadora import somar,subtrair, multiplicar, dividir


def executar_calculadora():

    operacoes = {
        "1": somar,
        "2": subtrair,
        "3": multiplicar,
        "4": dividir
    }

    while True:
        print("========CALCULADORA=========\n")
        print("********ESCOLHA UMA OPÇÂO********")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")

        opcao = input("Escolha uma opcao:")

        if opcao == "0":
            print("Programa finalizado")
            break

        if opcao not in operacoes:
            print("OPÇÂO INVALIDA")
            continue

        numero1 = float(input("Digite o primeiro valor: "))
        numero2 = float(input("Digite o segundo valor: "))

        funcao = operacoes[opcao]

        resultado = funcao(numero1, numero2)

        print(f"o resultado é {resultado}")

executar_calculadora()