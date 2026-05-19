#conversor de peso - modo fazendeiro
print("--- conversor de peso (kg ⇔ arroba) ===\n")

peso = float(input("digite o peso"))
unidade = input("é em K (quilos) ou A (arrobas)?")

if unidade == "k":
    arrobas = peso / 15
    print(peso, kg = arrobas:.2f, arrbas)
elif unidade == "A":
    quilos = peso * 15
    print(f"{peso} arrobas = {quilos:.2f} kg")
else:
    print("unidade inválida!")