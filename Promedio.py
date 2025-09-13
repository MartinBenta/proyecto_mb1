# Calular promedios.

def calcular_promedio(numeros):

    if not numeros:
        return 0
    return sum(numeros)/len(numeros)

notas = [7, 8, 9, 10, 10, 6, 4, 9]
promedio = calcular_promedio(notas)

print(f"El promedio es: {promedio}")