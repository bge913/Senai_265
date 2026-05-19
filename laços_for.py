procurar = input("o que procura?")
estoque = ["prego", "porca", "arruela", "parafuso", "mola"]
for i in estoque:
    if item == procurar:
        print("item encontrado no estoqie!")
        break # Inverrompe o laço imesiatamente
else:
    print("Item não encontrado após varredura copleta.")