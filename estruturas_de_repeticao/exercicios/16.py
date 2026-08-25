def validar_senha(senha_correta):
    tentativas = 3
    while tentativas > 0:
        senha_digitada = input("Digite a senha: ")
        if senha_digitada == senha_correta:
            return "Acesso permitido"
        tentativas -= 1
    return "Acesso bloqueado"

senha_correta = input("Defina a senha: ")
print(validar_senha(senha_correta))
