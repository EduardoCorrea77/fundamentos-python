def aluno():
    aluno = {
        'nome': 'Carlos',
        'notas': [8.0, 7.5, 9.0]
    }

    print(aluno['nome'])
    print(aluno['notas'])
    print(max(aluno['notas']))
    print(min(aluno['notas']))
    print(sum(aluno['notas']) / len(aluno['notas']))

aluno()