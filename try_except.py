# while True:
#     try:
#         edad = int(input("Ingrese su edad: "))
#         break
#     except ValueError as e:
#         print("Solo se aceptan números enteros")
#         print(e)
# print("Su edad es", edad)



# for i in range(10):
#     n1 = int(input("Ingrese un número: "))
#     if n1 % 2 != 0:
#         break


# suma = 0
# while True:
#     try:
#         num = int(input("Ingrese un número: "))
#         suma += num
#         if num == 0:
#             break
#     except:
#         print("Solo números enteros")
# print(f"La suma de los números es {suma}: ")

op = 0
while op != 4:
    uno = 70000
    dos= 500000
    tres = 580000
    iva = 1.19
    total = 0
    while True:
        try:
            print(f"1. Radio estereo SONY {uno}\n2. LGTV 55 pulgadas Super gamer {dos} \n3. PS5 {tres} \n4. Salir")
            op = int(input("Seleccione una opción "))

            match op:
                case 1:
                    print(f"El precio a pagar es  {uno * iva}")
                    total += (uno * iva)
                    print("----------------------------")
                case 2:
                    print("El precio a pagar es ", dos * iva)
                    total += dos * iva
                    print("----------------------------")
                case 3:
                    print("El precio a pagar es ", tres * iva)
                    total += tres * iva
                    print("----------------------------")
                case 4:
                    print(f"Total a pagar es {total}")
                    print("----------------------------")
                case _:
                    print("Opción Inválidad") #opción por defecto
        except ValueError:
            print("Solo puede ingresar números enteros")





























        