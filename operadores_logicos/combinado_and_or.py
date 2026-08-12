def show_veigh():
    POSSUI_INGRESSO = True
    idade = int(input("Qual a sua idade?: "))
    nome_lista = bool(input("Qual nome esta na lista?: "))

    posso_entra = idade >= 18 and nome_lista or POSSUI_INGRESSO

    print(f"vou consegir entrar no show?: {posso_entra}")

show_veigh()