# calculadora básica
print("=== Calculadora ===\n")

num1 =float(input("Digite o primeiro número:"))
operador = input("Digite o operador: (+, -, /, *)")
num2 = float(input("digite o segundo número: "))

if operador == "+":
    print(num1+num2)

elif operador == "-":
    print(num1-num2)

elif operador == "/":
    if num2 == 0:
        print("não dá dividir por zero")
    else:
        print(num1/num2)

elif operador == "*":
    print(num1*num2)

else: 
    print("operdor não reconhecido")