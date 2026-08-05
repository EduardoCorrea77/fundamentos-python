def salario():
    valor_hora = float(input("digite o valor da hora: "))
    horas_trabalhadas = float(input("digite a quantidade de horas trabalhadas: "))
    salario = valor_hora * horas_trabalhadas
    print(f"o salario e de {salario}")
salario()