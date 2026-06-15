'''
crear un gestr de estacionamiento
1 estacionamiento tiene 4 pisos
cada piso tiene 10 espacios

preguntar al ingresar un vehiculo:

que tipo de vehiculo es:
- ligero 2000
- mediano 3000
- pesado 3500

luego, acomodar en algun lugar de algún piso disponible
el menú debe tener:

1. Ingreso de Vehiculo
2. contar ganancias
3. contar vehiculos (puede ser total o total por piso)
4. ganancia promedio
'''



estacionamiento = {
    1 : [],
    2 : [],
    3 : [],
    4 : []
}

ligeros = []
medianos = []
pesados = []

cant_lig = 0
cant_med = 0
cant_pes = 0

total = 0

def ingreso_vehiculo(suma1, suma2, suma3):
    print("-"*30)
    while True:
        vehiculo = input("Indica que vehiculo quieres ingresar \n : ")
        tipo_vehiculo = input("Indica que tipo de vehiculo es: \n1. ligero \n2. mediano \n3. pesado \n : ")
        match tipo_vehiculo:
            case "1":
                ingreso_piso(vehiculo, tipo_vehiculo) 
                suma1.append(2000)
                break
            case "2":
                ingreso_piso(vehiculo, tipo_vehiculo)
                suma2.append(3000)
                break
            case "3":
                ingreso_piso(vehiculo, tipo_vehiculo)
                suma3.append(3500)
                break
            case _:
                print("Ingreso Inválido")
                continue
        

def ingreso_piso(vehiculo, tipo):
    while True:
        if tipo == "1": tipo = "ligero" 
        elif tipo == "2": tipo = "mediano" 
        elif tipo == "3": tipo = "pesado" 
        try:
            piso = int(input("Indique en que piso quiere estacionar el vehiculo (1, 2, 3 o 4)\n : "))
        except ValueError:
            print("Ingreso Inválido")
            continue
        if piso < 0 or piso > 4:
            print("Ingreso Inválido")
            continue
        if len(estacionamiento[piso]) >= 10:
            print("Piso lleno")
            continue
        else:
            estacionamiento[piso].append({'vehiculo' : vehiculo, 'tipo' : tipo})
            print(f"El vehiculo {vehiculo} fue estacionado en el piso °{piso} piso")
        for pisos, espacios in estacionamiento.items():
            print(f"Piso {pisos} | Vehiculos:",*espacios, sep=' ')
        break

def contar_ganancias(suma1, suma2, suma3):
    print("-"*30)
    total = sum(suma1) + sum(suma2) + sum(suma3)
    print(f"Total acumulado de ${total} pesos")
    return total

def contar_vehiculos():
    print("-"*30)
    total_autos = 0
    for pisos , espacios in estacionamiento.items():
        total_estacionados = len(espacios)
        total_autos += total_estacionados
        print(f"Piso {pisos} : {total_estacionados} vehiculos")
    print(f"Hay un total de {total_autos} vehiculos")

def ganancia_promedio(suma1, suma2, suma3):
    print("-"*30)
    total = sum(suma1) + sum(suma2) + sum(suma3)
    for pisos , espacios in estacionamiento.items():
        total_estacionados = len(espacios)
        total_autos += total_estacionados
    promedio = total/total_autos
    print(f"La ganancia promedio por vehiculo es de ${promedio} pesos")

def desvincular_vehiculo():
    print("-"*30)
    for pisos, espacios in estacionamiento.items():
        print(f"Piso {pisos} | Vehiculos:",*espacios, sep=' ')
    piso = input("Indique en que piso desvincular un vehiculo: ")
    match piso:
        case "1":
            del_vehiculo = input("Indique que vehiculo desea eliminar: ")         
        case "2":
            print("hola")
        case "3":
            print("hola")
        case _:
            print("Ingreso Inválido")

while True:
    print("-"*30)
    print("Estacionamiento")
    print("1. Ingreso de Vehiculo \n2. contar ganancias \n3. contar vehiculos (puede ser total o total por piso) \n4. ganancia promedio \n5. Desvincuar vehiculo\n6. Salir")
    try:
        op = input("Selecciona una acción: ")
        match op:
            case "1":
                ingreso_vehiculo(ligeros, medianos, pesados)
            case "2":
                contar_ganancias(ligeros, medianos, pesados)
            case "3":
                contar_vehiculos()
            case "4":
                ganancia_promedio(ligeros, medianos, pesados)
            case "5":
                # desvincular_vehiculo()
                print("hola")
            case "6":
                break
            case _:
                print("Ingreso Inválido")
    except KeyboardInterrupt:
        print("Sistema Bloqueado")
        break

