def jogo_adivinhacao(numero_secreto):
    palpite = 0

    while palpite != numero_secreto:
        palpite = int(input("Digite seu palpite: "))

        if palpite > numero_secreto:
            print("O palpite é maior que o número secreto.")

        elif palpite < numero_secreto:
            print("O palpite é menor que o número secreto.")

        else:
            print("Parabéns! Você acertou!")


numero_secreto = 7

jogo_adivinhacao(numero_secreto)

