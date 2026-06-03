
#-----------------------------------------------------------sin argumento | sin retorno

# def saludo():
#     print("Hola, que tal")


#-----------------------------------------------------------sin argumento | con retorno
# def suma():
#     num1 = 3
#     num2 = 5
#     return(num1 + num2)

# resultado = suma()
# print(resultado)

# def esMayor():
#     edad = 24
#     if edad >= 18:
#         return True
#     else:
#         return True

# print(esMayor())

#-----------------------------------------------------------con argumento | sin retorno

# def saludame(name):
#     print(f"Hola, {name}")

# saludame("rafa")

# def calculaIVA(neto):
#     print(f"El precio con IVA es {neto*1.19}")

# calculaIVA(1000)

#-----------------------------------------------------------con argumento | con retorno


def sumaCA(n1, n2):
    return(n1 + n2)


def calculaIVAca(neto):
    return neto*1.19

# print(f"El resultado es: {sumaCA(7, 10)}")
# # print(f"El total con IVA es: {calculaIVAca(10000)}")

# v = int(input("Ingrese el valor neto: "))

# print(f"El total con IVA es: {calculaIVAca(v)}")

def calculaDescuento(valor, desc):
    return valor - (valor*desc/100)

datos = [20500, 22]
print("El valor con descuento es: ", calculaDescuento(*datos))

