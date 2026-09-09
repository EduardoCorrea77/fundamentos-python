def alunos():
    lista = []

    for i in range(5):
        aluno = {}

        aluno['nome'] = input('Nome: ')
        aluno['idade'] = int(input('Idade: '))
        aluno['nota'] = float(input('Nota: '))

        lista.append(aluno)
    for aluno in lista:
        print(aluno)

alunos()