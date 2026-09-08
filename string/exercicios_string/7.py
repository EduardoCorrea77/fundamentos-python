def procurar_palavra(texto, palavra):
    posicao_palavra = texto.lower().find(palavra.lower())

    if posicao_palavra == -1:
        print("A palavra não existe no texto")
    else:
        print(f"A palavra começa na posição: {posicao_palavra}")

texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")

procurar_palavra(texto, palavra)