
notas = [7.5, 6.0, 8.5, 9.0, 5.5]

def adicionar_nota(notas, nota):
    notas.append(nota)
    print(f"Nota adicionada: {nota}")

def inserir_nota(notas, nota, posicao):
    notas.insert(posicao, nota)
    print(f"Nota {nota} inserida na posição {posicao}")

def adicionar_varias_notas(notas, novas_notas):
    notas.extend(novas_notas)
    print(f"Notas adicionadas: {novas_notas}")

def remover_nota(notas, nota):
    notas.remove(nota)
    print(f"Nota removida: {nota}")

def remover_ultima_nota(notas):
    nota_removida = notas.pop()

    print(f"Última nota removida: {nota_removida}")

    return nota_removida

def encontrar_nota(notas, nota):
    posicao = notas.index(nota)

    print(f"A nota {nota} está na posição {posicao}")

    return posicao

def quantidade_notas(notas):
    quantidade = len(notas)

    print(f"Quantidade de notas: {quantidade}")

    return quantidade

def ordenar_notas(notas):
    notas_ordenadas = sorted(notas)

    print(f"Notas ordenadas: {notas_ordenadas}")

    return notas_ordenadas

def inverter_notas(notas):
    notas_invertidas = list(reversed(notas))

    print(f"Notas invertidas: {notas_invertidas}")

    return notas_invertidas

def somar_notas(notas):
    soma = sum(notas)

    print(f"Soma das notas: {soma}")

    return soma

def calcular_media(notas):
    soma = sum(notas)

    quantidade = len(notas)

    media = soma / quantidade

    print(f"Média da turma: {media}")

    return media

print(f"Lista inicial: {notas}")

adicionar_nota(notas, 8.0)
print(notas)

inserir_nota(notas, 7.0, 2)
print(notas)

adicionar_varias_notas(notas, [6.5, 9.5])
print(notas)

remover_nota(notas, 5.5)
print(notas)

remover_ultima_nota(notas)
print(notas)

encontrar_nota(notas, 8.5)

quantidade_notas(notas)

ordenar_notas(notas)

inverter_notas(notas)

somar_notas(notas)

calcular_media(notas)