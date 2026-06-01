

productos = [

]
op = 0
while True:
    try:
        try:
            print("-"*25)
            print(f"1. Agregar producto \n2. Mostrar productos \n3. Eliminar productos \n4. Salir")
            op = int(input("Seleccione una opción "))
        except ValueError:
            print("Solo ingresar los opciones del menú")
        match op:
            case 1:
                while True:
                    print("-"*25)
                    nombre = input("Ingresa el producto que quieres agregar \nPara volver al menú principal ingresa -> back \n : ").lower()
                    if nombre != "back":
                        while True:
                            try:
                                precio = int(input(f"Ingresa el precio de {nombre}: "))
                                if precio < 0:
                                    print("Solo puedes ingresar números enteros positivos")
                                    continue
                                break
                            except ValueError:
                                print("Solo puede ingresar números enteros")
                        new_producto = {'nombre' : nombre, 'precio' : precio}
                        productos.append(new_producto)
                    else:
                        break
            case 2:
                print("Productos ingresados:")
                for producto in productos:
                    print(f"--|{producto['nombre']}, {producto['precio']}")
            case 3:
                print("SKU")
                i = 0
                for diccionario in productos:
                    print(f"{i}----{diccionario['nombre']} : {diccionario['precio']}")
                    i += 1
                while True:
                    try:
                        del_producto = int(input("Ingresa el SKU del producto que deseas eliminar: "))
                        if del_producto < 0:
                            print("No existe el SKU ingresado")
                            continue
                        else:
                            del productos[del_producto]
                            break
                    except (ValueError, IndexError):
                            print("No existe el SKU ingresado")
            case 4:
                print("Saliendo de la tienda...")
                break
            case _:
                print("Ingreso Inválido")
    except KeyboardInterrupt:
        print("--[Sistema Bloqueado]--")
        break

