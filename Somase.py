# Funcões com *args - calculadora flexível
def estatisticas(*numeros):
    total = sum(numeros)
    media = total / len(numeros)
    maximo = max(numeros)
    minimo = min(numeros)
    print(f"Total: {total} | Média: {media:.2f} | Máx: {maximo} | Mín: {minimo}")

estatisticas(59,68,80,90,46) #Tuplas
estatisticas(70,89,49) #Tuplas
# lista 
lista = [80,90,95] # Lista
estatisticas(*lista)