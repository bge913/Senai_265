n1 = float(input("digite a nota1"))
n2 = float(input("digite a nota2"))
n3 = float(input("digite a nota3"))
n4 = float(input("digite a nota4"))

Soma = (n1 + n2 + n3 + n4)
Media = (Soma / 4.0)

print(Media)

if Media >= 7:
    print("Aprovado")
elif Media >= 5:
    print("Recuperação")
else:
    print("Reprovado")