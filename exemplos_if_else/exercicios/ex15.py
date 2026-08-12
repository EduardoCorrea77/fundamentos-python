def velocidade():
    velocidade = float(input("Qual a velocidade do veículo? "))

    if velocidade <= 60:
        print("Velocidade permitida")
    elif velocidade <= 80:
        print("Atenção: velocidade acima do permitido")
    elif velocidade > 80:
        print("Multa por excesso de velocidade")


velocidade()