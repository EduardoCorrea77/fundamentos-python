def notas():
    aluno = {}

    aluno['nome'] = input('Nome: ')
    aluno['nota1'] = float(input('Nota 1: '))
    aluno['nota2'] = float(input('Nota 2: '))
    aluno['nota3'] = float(input('Nota 3: '))

    aluno['media'] = (aluno['nota1'] + aluno['nota2'] + aluno['nota3']) / 3

    print(aluno)

notas()