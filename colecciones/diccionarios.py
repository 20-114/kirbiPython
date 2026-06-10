# USO Y EXPLICACIÓN DE DICCIONARIOS

# alumno = {
#     "nombre" : "Kirbi",
#     "edad" : 14,
#     "carrera" : "Piloto"
# }

# print(alumno)
# print(alumno["carrera"])

# for key, value in alumno.items():
#     print(key, value)

# alumno["email"] = "kirbi@gmail.com"
# alumno["carrera"] = "escritor"
# del alumno["edad"]
# for key, value in alumno.items():
#     print(f"{key} = {value}")

#DICCIONARIO CON DICCIONARIOS

# productos = {
#     1:{"nombre" : "Control Inalambrico",
#     "categoria" : "Electronica",
#     "precios" : 45000},
#     2:{"nombre" : "Pilas recargables",
#     "categoria" : "Insumos",
#     "precios" : 5000},
#     3:{"nombre" : "Pasta termica",
#     "categoria" : "Computación",
#     "precios" : 10000}
# }


# print(productos[1]["precios"])

'''diccionarios'''

vegetales = {
    1 : 'Maracuya',
    2 : 'Pera',
    3 : 'Cebolla',
    4 : 'Papa'
}

# def agregarVegetal():
#     print("-"*25)
#     agregar = input("Ingrese un vegetal: ")
#     llave = list(vegetales.keys())[-1]   
#     vegetales[llave+1] = agregar

# def eliminarVegetal():
#     print("-"*25)
#     mostrarVegetales()
#     eliminar = int(input("Indica que el número de vegetal que deseas eliminar: "))
#     del vegetales[eliminar]

# def actualizarVegetales():
#     print("-"*25)
#     mostrarVegetales()
#     update = int(input("Ingresa el número del vegetal que deseas actualizar: "))
#     updateVegetal = input("Ingrese el nuevo vegetal: ")
#     vegetales[update] = updateVegetal
 
# def mostrarVegetales():
#     print("-"*25)
#     for num, nombre in vegetales.items():
#         print(f"{num}.- {nombre}")

# def vegetalesMenu():
#     while True:
#         print("-"*25)
#         try:
#             print("1. Agergar vegetales")
#             print("2. Eliminar vegetales")
#             print("3. Actualizar vegetales")
#             print("4. Mostrar vegetales")
#             print("5.  Salir")
#             op = int(input("Selecciona un aopción: "))
#             match op:
#                 case 1:
#                     agregarVegetal()
#                 case 2:
#                     eliminarVegetal()
#                 case 3:
#                     actualizarVegetales()
#                 case 4:
#                     mostrarVegetales()
#                 case 5:
#                     break
#                 case _:
#                     print("Opción Inválida")
#         except:
#             print("Opción indálida")

# vegetalesMenu()

'''Diccionario con diccionarios'''

productosDicc = {
    1 : {'nombre' : 'Maracuya', 'precio' : 3000},
    2 : {'nombre' : 'Pera', 'precio' : 3000},
    3 : {'nombre' : 'Cebolla', 'precio' : 3000}
}

print(productosDicc.keys())
print(productosDicc.values())
print(productosDicc.items())
def agregarVegetal():
    print("-"*25)
    agregarVeg = input("Ingrese un vegetal: ")
    agregarPrecio = int(input("Ingrese el precio del nuevo vegetal: "))
    llave = list(productosDicc.keys())[-1]   
    productosDicc[llave+1] = {'nombre': agregarVeg, 'precio' : agregarPrecio}

def eliminarVegetal():
    print("-"*25)
    mostrarVegetales()
    eliminar = int(input("Indica que el número de vegetal que deseas eliminar: "))
    del productosDicc[eliminar]

def actualizarVegetales():
    print("-"*25)
    mostrarVegetales()
    update = int(input("Ingresa el número del vegetal que deseas actualizar: "))
    upd = int(input("1.-Actualizar nombre \n2.-Actualizar precio \n : "))
    match upd:
        case 1:
            updateVegetal = input("Ingrese el nuevo vegetal: ")
            productosDicc[update]['nombre'] = updateVegetal
        case 2:
            updatePrecioVegetal = int(input("Ingrese el nuevo precio: "))
            productosDicc[update]['precio'] = updatePrecioVegetal
        case _:
            print("Inrgeso Inválido")

def mostrarVegetales():
    print("-"*25)
    for num, nombre in productosDicc.items():
        print(f"{num}.- {nombre['nombre']} = {nombre['precio']}")

def vegetalesMenuDicc():
    while True:
        print("-"*25)
        try:
            print("1. Agergar vegetales")
            print("2. Eliminar vegetales")
            print("3. Actualizar vegetales")
            print("4. Mostrar vegetales")
            print("5.  Salir")
            op = int(input("Selecciona un opción: "))
            match op:
                case 1:
                    agregarVegetal()
                case 2:
                    eliminarVegetal()
                case 3:
                    actualizarVegetales()
                case 4:
                    mostrarVegetales()
                case 5:
                    break
                case _:
                    print("Opción Inválida")
        except:
            print("Opción indálida")

vegetalesMenuDicc()

'''lista con diccionario'''

# productosListDicc = [
#     {'nombre' : 'Maracuya', 'precio' : 3000},
#     {'nombre' : 'Pera', 'precio' : 3000},
#     {'nombre' : 'Cebolla', 'precio' : 3000}
# ]

# def agregarVegetal():
#     print("-"*25)
#     agregarVeg = input("Ingrese un vegetal: ")
#     agregarPrecio = int(input("Ingrese el precio del nuevo vegetal: "))
#     productosListDicc.append({'nombre': agregarVeg, 'precio' : agregarPrecio})

# def eliminarVegetal():
#     print("-"*25)
#     mostrarVegetales()
#     eliminar = int(input("Indica que el número de vegetal que deseas eliminar: "))
#     productosListDicc.pop(eliminar)

# def actualizarVegetales():
#     print("-"*25)
#     mostrarVegetales()
#     update = int(input("Ingresa el número del vegetal que deseas actualizar: "))
#     upd = int(input("1.-Actualizar nombre \n2.-Actualizar precio \n : "))
#     match upd:
#         case 1:
#             updateVegetal = input("Ingrese el nuevo vegetal: ")
#             productosListDicc[update]['nombre'] = updateVegetal
#         case 2:
#             updatePrecioVegetal = int(input("Ingrese el nuevo precio: "))
#             productosListDicc[update]['precio'] = updatePrecioVegetal
#         case _:
#             print("Inrgeso Inválido")
 
# def mostrarVegetales():
#     print("-"*25)
#     for nombre in productosListDicc:
#         print(f"{productosListDicc.index(nombre)}.- {nombre['nombre']} = {nombre['precio']}")

# def vegetalesMenuList():
#     while True:
#         print("-"*25)
#         try:
#             print("1. Agergar vegetales")
#             print("2. Eliminar vegetales")
#             print("3. Actualizar vegetales")
#             print("4. Mostrar vegetales")
#             print("5.  Salir")
#             op = int(input("Selecciona un aopción: "))
#             match op:
#                 case 1:
#                     agregarVegetal()
#                 case 2:
#                     eliminarVegetal()
#                 case 3:
#                     actualizarVegetales()
#                 case 4:
#                     mostrarVegetales()
#                 case 5:
#                     break
#                 case _:
#                     print("Opción Inválida")
#         except:
#             print("Opción indálida")

# vegetalesMenuList()


