def login():
    usuario = input("Digite o usuário: ")
    senha = input("Digite a senha: ")

    if usuario == "admin" and senha == "1234":
        print("Login realizado com sucesso")
    elif senha != "1234":
        print("Senha incorreta")
    else:
        print("Usuário não encontrado")


login()