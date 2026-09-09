def somar_numeros():
    total = 0
    for valor in range(1,20):
        total += valor
        print(total)
# somar_numeros()

def mostrar_numeros_pares():
    for numero in range(1,21):
        if numero % 2 == 0:
            print(f"numeros pares: {numero}")
# mostrar_numeros_pares()

def mostrar_itens_lista():
    tabela_de_frutas = ("maçã", "banana", "pera", "abacaxi")
    print(f"minha sacola contem {tabela_de_frutas}")
# mostrar_itens_lista()

def laco_aninhado():
    nomes = ["Renam", "Moises", "Rafael"]
    notas = [8,9,10]
    for nome in nomes:
        print(f"nome do aluno: {nome}")
        for nota in notas:
            print(f"nota do aluno: {nota}")
laco_aninhado()

