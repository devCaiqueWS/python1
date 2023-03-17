
'''
maca = float(0.50)
cadastro = input("Você está cadastrado? s ou n: ")
qntdd = int(input("Quantas maçãs deseja comprar? : "))

if cadastro == "s" or qntdd>=20:
    maca = float(0.35)
    print(f"Valor total: {maca*qntdd}")
else:
    print(f"Valor total: {maca * qntdd}")

'''

senha = 12345
usuario = "admin"

user = input("Usuário: ")
pswrd = int(input("Senha: "))

if user == usuario and pswrd == senha:
    print(f"Bem vindo {usuario}!!! :)")
elif user == usuario and pswrd != senha:
    rede = input("Deseja redefinir sua senha? (s/n): ")
    if rede == "s":
        senha = int(input("Qual sua nova senha? : "))
        print(f"Sua nova senha : {senha}")
    else:
        print("Então escreve a senha certa FDP!!!")
elif user != usuario and pswrd == senha:
    print("Usuário ou Senha incorretos!!!")

else:
    print("KKKKKKKKKK Burro pra krl KKKKKKKKKK")