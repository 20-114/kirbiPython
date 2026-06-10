productosListDicc = [
    {'nombre' : 'Maracuya', 'precio' : 3000},
    {'nombre' : 'Pera', 'precio' : 3000},
    {'nombre' : 'Cebolla', 'precio' : 3000}
]

canasta = []
total = 0
def agregarVegetal():
    print("-"*25)
    agregarVeg = input("Ingrese un vegetal: ")
    agregarPrecio = int(input("Ingrese el precio del nuevo vegetal: "))
    productosListDicc.append({'nombre': agregarVeg, 'precio' : agregarPrecio})

def eliminarVegetal():
    print("-"*25)
    mostrarVegetales()
    eliminar = int(input("Indica que el número de vegetal que deseas eliminar: "))
    productosListDicc.pop(eliminar)

def actualizarVegetales():
    print("-"*25)
    mostrarVegetales()
    update = int(input("Ingresa el número del vegetal que deseas actualizar: "))
    upd = int(input("1.-Actualizar nombre \n2.-Actualizar precio \n : "))
    match upd:
        case 1:
            updateVegetal = input("Ingrese el nuevo vegetal: ")
            productosListDicc[update]['nombre'] = updateVegetal
        case 2:
            updatePrecioVegetal = int(input("Ingrese el nuevo precio: "))
            productosListDicc[update]['precio'] = updatePrecioVegetal
        case _:
            print("Inrgeso Inválido")
 
def mostrarVegetales():
    print("-"*25)
    for nombre in productosListDicc:
        print(f"{productosListDicc.index(nombre)}.- {nombre['nombre']} = {nombre['precio']}")

def mostrar_boleta():
    print("-"*25)
    for producto in canasta:
        print(producto)

def comprar_productos():
    mostrarVegetales()
    productos = int(input("Ingrese el número del producto que desea comrpar"))
    canasta.append({productosListDicc[productos]['nombre'] : productosListDicc[productos]['precio']})
    mostrar_boleta()

def vegetalesMenuList():
    while True:
        print("-"*25)
        # try:
        print("1. Agergar vegetales")
        print("2. Eliminar vegetales")
        print("3. Actualizar vegetales")
        print("4. Mostrar vegetales")
        print("5. Comprar Productos")
        print("6.  Salir")
        op = int(input("Selecciona un aopción: "))
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
        #     print("Opción indálida")

vegetalesMenuList()


# dicc = {'nombre':'rafa'}

# dicc['apellido'] = 'chacon'

# canasta.append()