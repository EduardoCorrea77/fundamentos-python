def validar_especie(animal):
    especie_valida = animal.isalpha()

    if especie_valida:
        print("Espécie de animal válida.")
    else:
        print("Espécie inválida.")

animal = input("Digite uma espécie de animal: ")

validar_especie(animal)