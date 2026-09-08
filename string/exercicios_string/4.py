def limpar_texto(texto):
    texto_limpo = texto.strip()
    return texto_limpo

texto = input("Digite um texto com espaços no início e no final: ")

print(f"Texto antes: {texto}")
print(f"Texto depois: {limpar_texto(texto)}")