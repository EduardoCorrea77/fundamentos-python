def tempeatura():
    tempeatura = int(input("insira uma temperatura em graus celsius: "))
    if tempeatura < 15:
        print("Frio")
    elif tempeatura >= 15 and tempeatura == 25:
        print("Agradavel")
    elif tempeatura > 25:
        print("Quente")
tempeatura()
