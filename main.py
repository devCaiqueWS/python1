

maca = float(0.50)
cadastro = input("Você está cadastrado? s ou n: ")
qntdd = int(input("Quantas maçãs deseja comprar? : "))

if cadastro == "s" or qntdd>=20:
    maca = float(0.35)
    print(f"Valor total: {maca*qntdd}")
else:
    print(f"Valor total: {maca * qntdd}")