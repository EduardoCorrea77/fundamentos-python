def separar_nome(nome_completo):
    partes = nome_completo.split()
    return partes

nome_completo = input("Digite seu nome completo: ")
print(f"Nome em Partes: {separar_nome(nome_completo)}")

def criar_nome_completo(partes):
    nome_completo = " ".join(partes)
    return nome_completo

partes_nome = ["Manoel", "Thiago", "Matias", "de", "Moraes"]
print(f"a junção das palavras do nome é: {criar_nome_completo(partes_nome)}")

def analisar_url(url):
    inicia_com_https = url.startswith("https://")
    termina_com_br = url.endswith(".br")
    return inicia_com_https, termina_com_br

url = "https://www.gov.br"
tem_https, tem_br = analisar_url(url)
print(f"Utiliza https: {tem_https}")
print(f"Termina com .br: {tem_br}")


# Verificar se a string contem somente numeros
def validar_idade(idade):
    idade_valida = idade.isdigit()
    if idade_valida:
        print(f"O valor digitado e uma idade valida")
    else:
        print("digite somente numeros")

idade = input("Digite sua idade: ")
validar_idade(idade)

def validar_nome(nome):
    nome_valido = nome.isalpha()
    if nome_valido:
     print("O nome digitado é valido")
    else:
     print("digite somente letras")

nome = input("Digite um nome valido: ")
validar_nome(nome)

def validar_usuario(usuario):
    usuario_valido = usuario.isalnum()

    if usuario_valido:
        print("Usuário válido!!!")
    else:
        print("Utilize apenas letras e números!!!")

nome_usuario = input("Digite seu usuário: ")
validar_usuario(nome_usuario)

def analizar_frase(frase, palavra):
    frase_limpa = frase.strip().lower()

    qtde_caracteres = len(frase_limpa)
    qtde_palavras = len(frase_limpa.split())
    ocorrencia_palavra = frase_limpa.count(palavra)

    print(f"Frase completa: {frase_limpa}")
    print(f"Total de caracteres: {qtde_caracteres}")
    print(f"Total de palavras: {qtde_palavras}")
    print(f"Ocorrencia: {ocorrencia_palavra}")

frase_input = input("Digite uma frase: ")
ocorrencia_palavra = input("Digite uma palavra para contar a ocorrencia: ")
analizar_frase(frase_input, ocorrencia_palavra)

