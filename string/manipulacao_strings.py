 # Converter texto para maiusculas e minusculas
def formatar_nome(nome):
    # nome em maiusculo
    nome_maiusculo = nome.upper()

    # nome minusculo
    nome_minusculo = nome.lower()

    # nome prieira letra maiuscula
    nome_camel_case = nome_maiusculo.capitalize()

    return (nome_maiusculo, nome_minusculo, nome_camel_case)

nome = input("Digite seu nome: ")

# print(formatar_nome(nome)[1])

nome_maiusculo, nome_minusculo, nome_camel_case = formatar_nome(nome)
print(f"Nome maiusculo: {nome_maiusculo}")
print(f"Nome minusculo: {nome_minusculo}")
print(f"Nome camel_case: {nome_camel_case}")

def limpar_texto(texto):
    #remove espaços no inicio e final do texto
    texto_limpo = texto.strip()
    return texto_limpo

texto_1 = "      Aprender Python é legal!!!  "
print(f"texto antes: {texto_1}")
print(f"texto depois: {limpar_texto(texto_1)}")

def  trocar_cidade(cidade):
    texto_trocado = cidade.replace(cidade, "Piracicaba")
    return texto_trocado

cidade = input("Digite seu cidade: ")
print(f"eu moro em :{trocar_cidade(cidade)}")

def analisar_texto(texto, letra):
    qtde_caracteres = len(texto)

    qtde_letra = texto.strip().lower().count(letra)

    return qtde_caracteres, qtde_letra

texto_2 = input("Digite seu texto: ")
letra = input("Digite uma letra: ")
caracteres, letras = analisar_texto(texto_2, letra)

print(f"total de caracteres: {caracteres}")
print(f"total de letras : {letras}")

def verificar_palavra(frase, palavra):
    palavra_presente = palavra.lower() in frase.lower()
    return palavra_presente
frase = input("Digite uma frase: ")
palavra = input("Digite uma palavra: ")

print(f"a palavra esta presente na frase: {verificar_palavra(frase, palavra)}")

def encontrar_posicao_palavra(frase, palavra):
    posicao_palavra = frase.lower().find(palavra.lower())
    return posicao_palavra

frase_2 = input("Digite uma nova frase: ")
palavra_2 = input("Digite uma palavra para saber sua posicao: ")

print(f"A posicao da palavra é {encontrar_posicao_palavra(frase_2, palavra_2)}")



