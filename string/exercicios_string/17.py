def limpar_telefone(telefone):
    telefone_limpo = telefone.replace("(", "")
    telefone_limpo = telefone_limpo.replace(")", "")
    telefone_limpo = telefone_limpo.replace(" ", "")
    telefone_limpo = telefone_limpo.replace("-", "")

    return telefone_limpo

telefone = input("Digite seu telefone: ")

print(f"Telefone limpo: {limpar_telefone(telefone)}")