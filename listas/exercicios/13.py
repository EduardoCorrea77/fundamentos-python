def adicionar_cliente(fila, cliente):
    fila.append(cliente)
    print(f"Cliente {cliente} entrou na fila")

def atender_cliente(fila):
    cliente_atendido = fila.pop(0)

    print(f"Cliente atendido: {cliente_atendido}")

    return cliente_atendido

fila = []

while True:
    cliente = input("Digite o nome do cliente ou digite sair: ")

    if cliente.lower() == "sair":
        break
    adicionar_cliente(fila, cliente)
print(f"Fila de clientes: {fila}")

if len(fila) > 0:
    atender_cliente(fila)
print(f"Fila atualizada: {fila}")