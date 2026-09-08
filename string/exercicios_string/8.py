def verificar_palavra(texto, palavra):
    palavra_presente = palavra.lower() in texto.lower()

    if palavra_presente:
        print("Palavra encontrada!")
    else:
        print("Palavra não encontrada!")

texto = input("Digite um texto: ")
palavra = input("Digite uma palavra: ")

verificar_palavra(texto, palavra)