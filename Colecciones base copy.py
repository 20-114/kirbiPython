#Funciones guia examen
 
 

'''
crar una función para mostrar todos los autos
'''
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}



def autos_vendidos_por_marca(marca, dicc):
    total_vendidos = 0
    for id, auto in dicc.items():
        if marca.lower() == auto[0].lower() and operaciones[id][1] != "Pendiente":
                total_vendidos += 1
    return f"Total {marca.lower().capitalize()} vendidos {total_vendidos}"

def  busqueda_por_anio(anio_min, anio_max):
    cumplen = []
    for id, auto in autos.items():
        if min <= auto[2] <= max and operaciones[id][1] == "Pendiente":
            cumplen.append(f"{auto[0]} {auto[1]}---{id}")
    if not cumplen:
        print("No se encontraron coincidencias")
    else:
        print(cumplen)
    
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones.keys():
        operaciones[id_auto][1] = nueva_fecha
        return True
    else:
        return False

while True:
    print('''
        ---Menú de Gestión---
1. Buscar vendidos por marca
2. Buscar existentes por rango de años
3. Actualiazar estado de venta
4. Incorporar nuevo vehículo
5. Dar de baja un vehículo
6. Salir
          ''')
    op = input("Selecciona una opción \n--|")
    match op:
        case "1":
            marca = input("Ingrese la marca que desea buscar \n--|")
            print(autos_vendidos_por_marca(marca, autos))
        case "2":
            while True:
                try:
                    min = int(input("Ingese el limite inferior \n--|"))
                    max = int(input("Ingese el limite superior \n--|"))
                except ValueError:
                    print("Solo puede ingresar números enteros")
                    continue
                busqueda_por_anio(min, max)
                break
        case "3":
            while True:
                id = input("Indica el id del vehículo que fue vendido\n--|").upper()
                fecha_venta = input("Indica la fecha de venta del vehículo")
                if actualizar_fecha_venta(id, fecha_venta):
                    print("Existo")
                else:
                    print("El identificador no existe")
                nuevo_ingreso = input("¿Desea actualizar otro vehículo (s/n)?\n--|").lower()
                if nuevo_ingreso == "s":
                    continue
                else:
                    break
        case "4":
            pass
        case "5":
            pass
        case "6":
            print("Saliendo del gestor...")
            break
        case _:
            print("Ingreso Inválido")
            continue
        

