from productos_tienda import productos
canasta = []
total_productos_canasta = 0
total_pagar = 0
print("-"*25)
print("SuperEccomers")
while True:
    try:
        op = int(input("1. Agregar producto a la canasta \n2. Ver canasta \n3. Salir de la tienda \n : "))
        match op:
            case 1:
                while True:
                    print("SKU")
                    i = 0
                    for producto in productos:
                        print(f"{i}----{producto['nombre']} : {producto['precio']}")
                        i += 1
                    print("Ingresa el SKU del producto que deseas agregar a la canasta")
                    print("Para volver al menú principal ingresa -> back")
                    add_producto = input(" : ").lower()
                    try:
                        if add_producto != "back":
                            add_producto = int(add_producto)
                        if add_producto != "back":
                            if add_producto < 0:
                                print("No existe el SKU ingresado")
                                continue
                            else:
                                canasta.append(productos[add_producto])
                                total_productos_canasta += 1
                                total_pagar += productos[add_producto]['precio']     
                        else:
                            break
                    except (IndexError):
                        print("No existe el SKU ingresado")
                    except (ValueError, TypeError):
                        print("Ingreso Inválido")
            case 2:
                while True:
                    print("-"*25)
                    sku = 0
                    for producto in canasta:
                        print(f"{sku} {producto['nombre']} : {producto['precio']}")
                        sku += 1
                    print(f"Total de productos en canasta: {total_productos_canasta}")
                    print(f"Total a pagar: {total_pagar}")
                    volver = int(input("1. Eliminar un producto de la canasta \n2. Volver"))
                    match volver:
                        case 1:
                            eliminar = int(input("¿Ingrese el SKU del producto que desea eliminar: "))
                            del canasta[eliminar]
                            total_productos_canasta -= 1
                            total_pagar -= canasta[eliminar]['precio']
                        case 2:
                            break
                        case _:
                            print("Ingreso Inválido")
            case 3:
                break
            case _:
                print("Ingreso Inválido")
    except KeyboardInterrupt:
        print("--|Sistema Bloqueado|--")



