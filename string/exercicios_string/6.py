def contar_letra(frase, letra):
    qtde_letra = frase.lower().count(letra.lower())
    return qtde_letra

frase = input("Digite uma frase: ")
letra = input("Digite uma letra: ")

print(f"A letra aparece {contar_letra(frase, letra)} vezes")