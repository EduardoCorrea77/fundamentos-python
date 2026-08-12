def nota():
    nota = int(input("Digite a sua nota: "))
    if nota >= 6:
        print("aprovado")
    elif nota < 6:
        print("reprovado")
nota()