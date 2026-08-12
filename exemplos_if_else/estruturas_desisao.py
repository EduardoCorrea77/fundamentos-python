def aluno_aprovado():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    media = (nota1 + nota2) / 2

    if media >= 6:
        print("Aprovado")
    elif media >= 5 and media <= 6:
        print("Recuperacao")
    else:
        print("Reprovado")
aluno_aprovado()




def login():
    e_mail = "aspas67@gmail.com"
    senha = "6742"
    codigo_secreto = "4267"

    e_mail_input = input("Digite o seu e-mail: ")
    senha_input = input("Digite sua senha: ")


    if e_mail_input == e_mail and senha_input == senha:
        print("Logado")
        acessar_admin = input("Deseja acessar o administrador? [S/N]")
        if acessar_admin == "S":
            codigo_secreto_input = input("Digite o seu codigo secreto: ")
            if codigo_secreto_input == codigo_secreto:
                print("acesso adm liberado")
            elif acessar_admin == "N":
                print("vc acessou como usuario comum")
            else:
                print("codigo secreto incorreto")
        else:
            print("opcao invalida")
    else:
        print("Email ou senha incorreto")
login()

