def filme():
    filme = {
        'titulo': 'Vingadores',
        'ano': 2019,
        'genero': 'Ação',
        'notas': []
    }
    for i in range(5):
        nota = float(input('Digite a nota: '))
        filme['notas'].append(nota)

    media = sum(filme['notas']) / len(filme['notas'])

    print(filme)
    print('Média:', media)

filme()