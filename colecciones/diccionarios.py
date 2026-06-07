# USO Y EXPLICACIÓN DE DICCIONARIOS

alumno = {
    "nombre" : "Kirbi",
    "edad" : 14,
    "carrera" : "Piloto"
}

print(alumno)
print(alumno["carrera"])

for key, value in alumno.items():
    print(key, value)

alumno["email"] = "kirbi@gmail.com"
alumno["carrera"] = "escritor"
del alumno["edad"]
for key, value in alumno.items():
    print(f"{key} = {value}")

#DICCIONARIO CON DICCIONARIOS

# productos = {
#     1:{"nombre" : "Control Inalambrico",
#     "categoria" : "Electronica",
#     "precios" : 45000},
#     2:{"nombre" : "Pilas recargables",
#     "categoria" : "Insumos",
#     "precios" : 5000},
#     3:{"nombre" : "Pasta termica",
#     "categoria" : "Computación",
#     "precios" : 10000}
# }


# print(productos[1]["precios"])

