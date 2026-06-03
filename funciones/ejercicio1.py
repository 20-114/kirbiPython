'''
Cree una función para pedir notas
y ponerlas en el argumento para sacar el promedio
'''

listaNotas = []

cantidadNotas = int(input("Ingrese la cantidad de notas: "))

for i in range(cantidadNotas):
    notas = listaNotas.append(float(input(f"Ingrese la {i+1}° nota: ")))


def promedio(lista):
    # suma = 0
    # for nota in listaNotas:
    #     suma += nota
    # promedio = suma/len(listaNotas)
    promedio = sum(lista)/len(lista)
    return promedio

print("El promedio de notas es ", promedio(listaNotas))



