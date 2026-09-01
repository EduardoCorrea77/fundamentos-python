def inserir_aluno(alunos, nome, posicao):
    alunos.insert(posicao, nome)


lista_alunos = ["Eduardo", "Felipe", "Kael", "Murillo"]
print(lista_alunos)

inserir_aluno(lista_alunos, "Manoel", 2)

print(lista_alunos)