import time

def mostrar_numero():
    for i in range(1,6):
        print(F"o numero atual e {i}")
        time.sleep(5)
mostrar_numero()

def mostrar_numero_alternado():
    for num in range(0,20,2):
        print(f"o numero atual e {num}")
mostrar_numero_alternado()
