def idade():
    idade = int(input("Quantos anos de idade você tem?: "))
    if idade >= 18:
        print("maior de idade")
    elif idade < 18:
        print("menor de idade")
idade()
