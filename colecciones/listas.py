#USO DE LISTAS

# lista = [8, 20, 12, 87]

# print(lista)
# print(lista[3])

# for elemento in lista:
#     print(f"Número: {elemento}")


# canasta = ["frutilla", "platano", "mora", "kiwi"]

# for elemento in canasta:
#     print(f"Fruta: {elemento}")

'''
Hacer una lista de nombres y otra de apellidos
Mostrar las listas como si fueran nombres completos
Vale decir, Diego Robles, Adolfo Hinako, Luis Mussolini
'''

# nombres = ["Pablo", "Felipe", "Maria"]
# apellidos = ["González", "Hermosilla", "Martinez"]

# nom = 0
# ape = 0
# while nom < 3:
#     print(nombres[nom], apellidos[ape])
#     nom += 1
#     ape += 1

# print(f"{nombres[0]} {apellidos[0]},{nombres[1]} {apellidos[1]},{nombres[2]} {apellidos[2]}")

# for n in range(len(nombres)):
#     print(nombres[n], apellidos[n])

# datos = [4, 6.9, "Patricio", False]

# for d in datos:
#     print(d)

# matrix = [
#     [5,8,3], [79,34,24]
# ]
# print(matrix[1][0])

# matrix = [
#     {'nombre': 'Rafa', 'notas': [45]},
#     {'nombre': 'Jorge', 'notas': [50]},
#     {'nombre': 'Ale', 'notas': [24]}
# ]
# dic = [
#     {'nombre': 'Rafa', 'notas': [45]},
#     {'nombre': 'Jorge', 'notas': [50]},
#     {'nombre': 'Ale', 'notas': [24]}
# ]
# dic = [
    # {
    #     'nombre': 'Rafa', 
    #     'notas': [45]
    # },
    # {'nombre': 'Jorge', 
    #  'notas': [30]
    # }
# ]
# for indx, elemento in enumerate(dic):
#     elemento['notas'].

# print(dic)

# 1. Tu estructura de datos inicial
personas = [
    {
        'nombre': 'Rafa', 
        'notas': [45]
    },
    {'nombre': 'Jorge', 
     'notas': [30]
    }
]

# 2. La lista de nuevos elementos que quieres añadir
nuevas_notas = 10
nombre = "Jorge"
# 3. Recorremos la lista con un for usando 'enumerate' para tener el índice
for indice, elemento in enumerate(personas):
    # Accedemos a la lista dentro del diccionario usando la clave y el índice
    # nuevo_elemento = nuevas_notas[indice]
    if nombre == elemento['nombre']:
        elemento['notas'].append(nuevas_notas)

# 4. Resultado final
print(personas)


