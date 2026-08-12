def pode_dirigir():
    idade = int(input("digite a idade: "))
    TEM_HABILITACAO = True

    autorizado = idade >= 18 and TEM_HABILITACAO

    print(f"usuario pode dirigir?: {autorizado}")

pode_dirigir()
