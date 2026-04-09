def calcular_media(lista):
    total = 0
    for i in range (len(lista)):
        total += lista[i]
    return total / len(lista)

notas = [7, 8, 9]
print(calcular_media(notas))

    