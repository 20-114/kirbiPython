'''
Objetivo del programa: Un programa funcional que, dada una lista de números
ingresada por el usuario, identifica y muestra los números pares e impares de
manera clara y organizada.

Reglas de negocio:

1. Solicitar al usuario que ingrese una lista de números enteros
separados por espacios.

2. Implementar una función llamada validar_lista_numeros que verifique
que todos los elementos ingresados sean números enteros. Si se
ingresa algún valor no válido, solicitar nuevamente la lista.

3. la función validar_lista_numeros debe utilizar un bucle y maneja
excepciones para asegurar que todos los elementos ingresados sean
números enteros.

4. Utilizar el operador de módulo % (MOD) para determinar si un
número es par o impar en la lista de números a ingresar. Considerar
que un número es par cuando el mod es igual a 0, en caso contrario,
es impar.

5. Crear dos listas separadas: una para los números pares y otra para
los impares.

6. Mostrar al usuario las listas resultantes, indicando los números
pares, e indicando los números impares
'''
print("Debes ingresar una lista de números")


# def ingreso_lista():
    # estado = "activo"
    # ingreso = lista
    # while estado == "activo":
    #     n = 1 
    #     while True:
    #         try:
    #             num = (input(f"Ingresa el {n}° número. \nIngresa LISTO cuando no quiereas agrega más números a tu lista. \n :  ")).upper()
    #             if num == "LISTO":
    #                 break
    #             else:
    #                 num = int(num)
    #                 ingreso.append(num)
    #                 n += 1
    #         except ValueError:
    #             print("Solo puedes ingresar números")


numeros = input("Ingrese una lista de números enteros separados por espacios: ")
lista = numeros.split(" ")

def validar_lista_números():
    for elemento in lista:
        if elemento in "1234567890":
            continue
        else:
            print("Al menos un lemento de la lista no es entero. Intenta de nuevo")
            break    

validar_lista_números()


print(lista)

