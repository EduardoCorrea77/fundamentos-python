def nota():
    nota = int(input("digite a sua nota: "))
    if nota <= 4:
        print("insuficiente")
    elif nota >= 5 and nota <=6:
        print("regular")
    elif nota >= 7 and nota <=8:
        print("bom")
    elif nota >= 9 and nota <=10:
        print("excelente")
nota()