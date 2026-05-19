login = input("Login")
senha = input("senha")

contador = 0
for i in range(3):
 print(i)
contador += 1
if login == "fudenço" and senha == "321654":
    print("Olá Fudencio! Tudo bem?")
else:
    print("Errado! Faça login")