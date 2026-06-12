productosListDicc = [
    {'nombre' : 'Maracuya', 'precio' : 3000},
    {'nombre' : 'Pera', 'precio' : 2500},
    {'nombre' : 'Cebolla', 'precio' : 3000}
]

canasta = []
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
    print("-"*25, 0, "-"*25)
    iva = 1.19
    total = 0
    for producto in canasta:
        print(producto['nombre'], ":", producto['precio'])
        total += producto['precio']
    total_con_iva = total * iva
    print("-"*25, 0, "-"*25)
    print(f"Total sin iva: {total} pesos")
    print(f"Total a pagar: {total_con_iva} pesos")

def comprar_productos():
    while True:
        mostrarVegetales()
        print("Escribe EXIT para salir")
        try:
            productos = input("Ingrese el número del producto que desea comrpar: ").upper()
            if productos.isdigit():
                productos = int(productos)
                canasta.append(productosListDicc[productos])
            elif productos == "EXIT":
                break
            else:
                print("Ingreso Inválido")
        except IndexError:
            print("El producto ingresado no existe")
            continue

def vegetalesMenuList():
    while True:
        print("-"*25)
        # try:
        print("1. Agergar vegetales")
        print("2. Eliminar vegetales")
        print("3. Actualizar vegetales")
        print("4. Mostrar vegetales")
        print("5. Comprar Productos")
        print("6. Crear Boleta (calcula IVA) y Salir")
        try:
            op = input('Selecciona una opción: ')
            match op:
                case '1':
                    agregarVegetal()
                case '2':
                    eliminarVegetal()
                case '3':
                    actualizarVegetales()
                case '4':
                    mostrarVegetales()
                case '5':
                    comprar_productos()
                case '6':
                    mostrar_boleta()
                    break
                case _:
                    print("Opción Inválida")
        except KeyboardInterrupt:
            print("Sistema Bloqueado")
            break

vegetalesMenuList()


# dicc = {'nombre':'rafa'}

# dicc['apellido'] = 'chacon'

# canasta.append()