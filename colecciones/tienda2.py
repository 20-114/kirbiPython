productosDicc = {
    1 : {'nombre' : 'Maracuya', 'precio' : 3000},
    2 : {'nombre' : 'Pera', 'precio' : 3000},
    3 : {'nombre' : 'Cebolla', 'precio' : 3000}
}

canasta = {}

# print(productosDicc.keys())
# print(productosDicc.values())
# print(productosDicc.items())
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

def mostrarCanasta():
    print("-"*25)
    for num, nombre in canasta.items():
        print(f"{num}.- {nombre['nombre']} = {nombre['precio']}")

def comprar_productos():
    mostrarVegetales()
    producto = int(input("Ingrese el numero del producto que desea comprar \n : "))
    prod = productosDicc[producto].values()
    canasta[prod] = {'nombre' : prod['nombre']}
    mostrarCanasta()


def vegetalesMenuDicc():
    while True:
        print("-"*25)
        # try:
        print("1. Agergar vegetales")
        print("2. Eliminar vegetales")
        print("3. Actualizar vegetales")
        print("4. Mostrar vegetales")
        print("5. Comprar vegetales")
        print("6. Salir")
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
                comprar_productos()
            case 6:
                break
            case _:
                print("Opción Inválida")
        # except:
        #     print("Opción inválida")


mostrarVegetales()
vegetalesMenuDicc()
