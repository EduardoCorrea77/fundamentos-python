def posso_comprar():
    TEM_CARTAO = False
    tem_dinheiro = bool(input("vc tem dinheiro para comprar?: "))
    autorizado = tem_dinheiro or TEM_CARTAO
    print(f"vou comer um MC-Donalds hoje?: {autorizado}")

posso_comprar()