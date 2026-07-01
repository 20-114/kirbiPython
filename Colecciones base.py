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

def mostrarAutos(dicc):
    print("----Listado de Autos----")
    for id, auto in dicc.items():
        print(f"id: {id} | caracteristicas: {auto}")
        


# auto = lambda auto : auto, autos
# print(auto)

#crear una función que muestre solo los autos vendidos

def mostrarAutosVendidos(autos):
    print("----Autos Vendidos----")
    for id, auto in autos.items():
        if not operaciones[id][1] == "Pendiente":
            print(f"id: {id} | {auto}")

# mostrarAutos(autos)
# mostrarAutosVendidos(autos)

def autosVendidosPorMarca(dicc, marca):
    vendidos = 0
    for id, auto in dicc.items():
        if marca.lower() in auto[0].lower():
            if not operaciones[id][1] == "Pendiente":
                vendidos += 1
    print(vendidos)

# marca = input("Marca a buscar: ")
# autosVendidosPorMarca(autos, marca)

def busqueda_por_anio(anio_min, anio_max):
    lista_anios = []
    for id, auto in autos.items():
        if anio_min < auto[2] < anio_max:
            lista_anios.append(f"{auto[0]} {auto[1]}---{id}")
    print(lista_anios)

# while True:
#     try:
#         min = int(input("Ingrese el año mínimo"))
#         max = int(input("Ingrese el año máximo"))
#     except Exception as e:
#         print(e)
#     busqueda_por_anio(min, max)
#     break


def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in autos:
        operaciones[id_auto][1] = nueva_fecha
        return True
    else: 
        return False

while True:  
    try: 
        id_auto = input("Ingrese el id del vehiculo")
        nueva_fecha = input("Ingrese la nueva fecha de venta")
        existencia = actualizar_fecha_venta(id_auto, nueva_fecha)
        if existencia:
            print(f"La fecha de venta del vehiculo {id_auto} fue actualizada correctamente")
        else:
            print(f"El id {id_auto} del vehiculo no existe")
        seguir = input("¿Desea actualizar otro vehiculo? (s/n)")
        if seguir == "s":
            continue
        else:
            break
    except Exception as e:
        print(e)

        

