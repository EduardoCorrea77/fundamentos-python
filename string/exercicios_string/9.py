def contar_palavras(texto):
    texto_limpo = texto.strip()
    palavras = texto_limpo.split()
    qtde_palavras = len(palavras)

    return qtde_palavras

texto = input("Digite um texto: ")

print(f"Quantidade de palavras: {contar_palavras(texto)}")