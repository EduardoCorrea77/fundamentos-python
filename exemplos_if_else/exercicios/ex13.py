def ingresso():
    idade = int(input("Qual a sua idade? "))

    if idade <= 5:
        print("Ingresso gratuito")
    elif idade <= 12:
        print("Ingresso: R$ 10,00")
    elif idade <= 59:
        print("Ingresso: R$ 20,00")
    else:
        print("Ingresso: R$ 10,00")


ingresso()
