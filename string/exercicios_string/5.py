def substituir_palavra(frase, palavra_1, palavra_2):
    texto_trocado = frase.replace(palavra_1, palavra_2)
    return texto_trocado

frase = input("Digite uma frase: ")
palavra_1 = input("Digite a palavra que deseja trocar: ")
palavra_2 = input("Digite a nova palavra: ")

print(f"Frase modificada: {substituir_palavra(frase, palavra_1, palavra_2)}")