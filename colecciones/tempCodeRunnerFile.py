    while True:
        agregarProducto = input("Ingrese un producto: ")
        for num_producto in productosDicc.values():
            if agregarProducto in num_producto.values():
                print("Ya existe el producto ingresado")
                continue
        break
    while True:
        try:
            agregarPrecio = int(input("Ingrese el precio del nuevo producto: "))
            llave = list(productosDicc.keys())[-1]
            productosDicc[llave+1] = {'nombre': agregarProducto, 'precio' : agregarPrecio}
            break
        except ValueError:
            print("Solo puede ingresar números")
            continue

