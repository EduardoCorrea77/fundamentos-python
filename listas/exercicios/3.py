def adicionar_convidados(convidados, novos_convidados):
    convidados.extend(novos_convidados)

lista_convidados = ["Eduardo", "Felipe"]
novos = ["Manoel", "Kael", "Murillo"]

adicionar_convidados(lista_convidados, novos)

print(lista_convidados)