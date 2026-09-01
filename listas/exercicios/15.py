def adicionar_nota(notas, nota):
    notas.append(nota)
    print(f"Nota adicionada: {nota}")
    print(f"Notas: {notas}")

def remover_nota(notas, nota):
    notas.remove(nota)
    print(f"Nota removida: {nota}")
    print(f"Notas atualizadas: {notas}")

def media_notas(notas):
    soma = sum(notas)
    quantidade = len(notas)

    media = soma / quantidade

    print(f"Média das notas: {media}")
    return media
notas = [7.5, 8.0, 6.5]
adicionar_nota(notas, 9.0)
remover_nota(notas, 6.5)
media_notas(notas)