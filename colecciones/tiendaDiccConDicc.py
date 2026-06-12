productosDicc = {
    1 : {'nombre' : 'Maracuya', 'precio' : 3000},
    2 : {'nombre' : 'Pera', 'precio' : 3000},
    3 : {'nombre' : 'Cebolla', 'precio' : 3000}
}

canasta = {}

# print(productosDicc.keys())
# print(productosDicc.values())
# print(productosDicc.items())
def agregarProducto():
    print("-"*25)
    while True:
        agregarProducto = input("Ingrese un producto: ")
        existe = False
        for num_producto in productosDicc.values():
            if agregarProducto in num_producto['nombre']:
                existe = True
                print("Ya existe el producto ingresado")
                break
        if existe == False: 
            break
        else:
            continue    
    while True:
        try:
            agregarPrecio = float(input("Ingrese el precio del nuevo producto: "))
            if agregarPrecio < 0:
                print("Solo números positivos")
                continue
            llave = list(productosDicc.keys())[-1]
            productosDicc[llave+1] = {'nombre': agregarProducto, 'precio' : agregarPrecio}
            break
        except ValueError:
            print("Solo puede ingresar números")
            continue


def eliminarProducto():
    print("-"*25)
    mostrarProducto()
    eliminar = int(input("Indica el número de producto que deseas eliminar: "))
    del productosDicc[eliminar]

def actualizarProducto():
    print("-"*25)
    mostrarProducto()
    update = int(input("Ingresa el número del producto que deseas actualizar: "))
    upd = int(input("1.-Actualizar nombre \n2.-Actualizar precio \n : "))
    match upd:
        case 1:
            updateVegetal = input("Ingrese el nuevo producto: ")
            productosDicc[update]['nombre'] = updateVegetal
        case 2:
            updatePrecioVegetal = int(input("Ingrese el nuevo precio: "))
            productosDicc[update]['precio'] = updatePrecioVegetal
        case _:
            print("Inrgeso Inválido")

def mostrarProducto():
    print("-"*25)
    for num, nombre in productosDicc.items():
        print(f"{num}.- {nombre['nombre']} = {nombre['precio']}")

def mostrarCanasta():
    print("-"*25)
    for num, nombre in canasta.items():
        print(num, nombre)
        # print(f"{num}.- {nombre['nombre']} = {nombre['precio']}")

def comprar_productos():
    while True:
        mostrarProducto()
        print("Presiona '0' para salir")
        try:
            num_producto = int(input("Ingrese el numero del producto que desea comprar \n : "))
            producto = productosDicc[num_producto]
            canasta[producto['nombre']] = producto['precio']
            print(f"El producto {producto['nombre']} se agrego a la canasta")
        except KeyError:
            break

def generar_boleta():
    print("-"*25)
def productosMenuDicc():
    while True:
        print("-"*25)
        try:
            print("1. Agergar vegetales")
            print("2. Eliminar vegetales")
            print("3. Actualizar vegetales")
            print("4. Mostrar vegetales")
            print("5. Comprar vegetales")
            print("6. Generar boleta (con IVA). Salir")
            op = int(input("Selecciona un opción: "))
            match op:
                case 1:
                    agregarProducto()
                case 2:
                    eliminarProducto()
                case 3:
                    actualizarProducto()
                case 4:
                    mostrarProducto()
                case 5:
                    comprar_productos()
                case 6:
                    generar_boleta()
                    break
                case _:
                    print("Opción Inválida")
        except KeyboardInterrupt:
            print("\nSistema Bloqueado")
            break

productosMenuDicc()


