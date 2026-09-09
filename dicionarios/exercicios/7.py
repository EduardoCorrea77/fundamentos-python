def verificar():
    aluno = {
        'nome': 'Eduardo',
        'media': 8,
        'frequencia': 80
    }

    if aluno['media'] >= 6 and aluno['frequencia'] >= 75:
        print('Aprovado')
    else:
        print('Reprovado')

verificar()