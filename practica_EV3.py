'''
PREGUNTAR CUANTOS JUEGOS SON
Debe preguntar al usuario Nombre del Juego:
 - al menos 5 caractres
 - no debe incluir espacios y todas mayusculas
 Preguntar precio:
 - solo numeros enteros positivos
 - Si vale más de 20000 es Indie, pero menos 40000
 - si vale 40000 o más, es de estudio
 - Mostrar al final cuantos hay de cada categoria
 Clasificación:
 -E para todos
 - +12 adolecentes
 - M para personas mayores
 -Mostrar resumen_
 Ej: hay 4 indie, y 5 de estudio. Solo 3 son clasificación E
'''

# indie = 0
# estudio = 0
# e = 0
# mas12 = 0
# m = 0
# while True:
#     try:
#         num_juejos = int(input("Indique cuantos juegos quiere registrar: "))
#         if num_juejos < 0:
#             print("Solo ingresar números enteros positivos")
#             continue
#         break
#     except:
#         print("Solo puede ingresar número enteros")

# for num in range(num_juejos):
#     while True:
#         nom_juego = input("Ingrese el nombre del juego: ")
#         if len(nom_juego) < 5:
#             print("Debe tener almenos 5 caracteres")
#             continue
#         if not nom_juego.isupper():
#             print("Solo utilizar mayusculas")
#             continue
#         if " " in nom_juego:
#             print("No debe incluir espacios")
#             continue
#         break


#     while True:
#         try:
#             precio = int(input("Ingrese el precio del juego: "))
#             if precio < 0:
#                 print("Solo puedes ingresar números positivos")
#                 continue
#             break
#         except ValueError:
#             print("Solo puedes ingresar números enteros")

#     while True:
#         try:
#             edad = int(input("Ingrese para que edad es el juego: "))
#             if precio < 0:
#                 print("Solo puedes ingresar números positivos")
#                 continue
#             break
#         except ValueError:
#             print("Solo puede ingresar números enteros")
    
#     if precio >= 20000 and precio < 40000:
#         indie += 1
#     elif precio >= 40000:
#         estudio += 1
#     elif precio == 0:
#         e += 1

#     if edad > 12 and edad < 18:
#         mas12 += 1
#     elif edad >= 18:
#         m += 1


# print(f'''Hay {indie} indie, y {estudio} de estudio. 
# Clasificaciones:
#     {e} Clasificación E 
#     {mas12} Clasificación +12
#     {m} Clasificación M''')
        


'''
Almacenamiento Biblioteca

Los espacios son noventa
Cada libro usa un espacio
===MENU PRINCIPAL===
1. Espacios disponibles
2. Poner libros
3. Sacar libros
4. Historial de ocupación
5. Salir

Historial de Ocupaciones
- Mostrar la cantidad de libros registrados en la biblioteca durante la sesión.
- Cada registro debe aumentar el historial
- Cada retiro debe disminuir el historiar
'''

import time

espacio = 90
while True:
    try:
        opc = int(input("Ingrese la acción a realizar \n1)Espacios disponibles\n2)Poner libro\n3)Sacar libro\n4)Historial de ocupaciones\n5)Salir\n: "))
    except ValueError:
        print("Solo puede ingresar números ")

    match opc:
        case 1:
            print(f"Espacios disponibles: {espacio}")
            print("-"*25)
            time.sleep(2)
        case 2:
            espacio -= 1
            print("Registro realizado correctamente")
            print("-"*25)
            time.sleep(2)
        case 3:
            espacio += 1
            print("Registro eliminado")
            print("-"*25)
            time.sleep(2)
        case 4:
            print(f"Espacios ocupados: {90 - espacio}")
            print("-"*25)
            time.sleep(2)
        case 5:
            print("Saliendo de la biblioteca...")
            break
        case _:
            print("Opción Invalida")
            print("-"*25)
            time.sleep(2)

