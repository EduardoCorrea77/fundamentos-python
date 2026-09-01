def adicionar_nome(nomes, nome):
    nomes.append(nome)
    for nome in nomes:
     print(f"o nome da lista e {nome}")

lista_nomes = ["eduardo", "felipe", "kael", "murillo"]
adicionar_nome(lista_nomes, "manoel")