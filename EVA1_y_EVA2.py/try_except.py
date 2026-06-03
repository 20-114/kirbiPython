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

# op = 0
# while op != 4:
#     uno = 70000
#     dos= 500000
#     tres = 580000
#     iva = 1.19
#     total = 0
#     while True:
#         try:
#             print(f"1. Radio estereo SONY {uno}\n2. LGTV 55 pulgadas Super gamer {dos} \n3. PS5 {tres} \n4. Salir")
#             op = int(input("Seleccione una opción "))

#             match op:
#                 case 1:
#                     print(f"El precio a pagar es  {uno * iva}")
#                     total += (uno * iva)
#                     print("----------------------------")
#                 case 2:
#                     print("El precio a pagar es ", dos * iva)
#                     total += dos * iva
#                     print("----------------------------")
#                 case 3:
#                     print("El precio a pagar es ", tres * iva)
#                     total += tres * iva
#                     print("----------------------------")
#                 case 4:
#                     print(f"Total a pagar es {total}")
#                     print("----------------------------")
#                 case _:
#                     print("Opción Inválidad") #opción por defecto
#         except ValueError:
#             print("Solo puede ingresar números enteros")

# -----------------------------------------------------------------------------------------------------------

'''
Simula un cajero automático con un saldo inicial de $100.000
Solo se puede sacar/ingresar montos multiplos de $5.000

El usuario puede:

1. consultar saldo
2. retirar dinero
3. depositar dinero
4. salir

debes usar try-except para manjar:

montos invalidos
retiro mayor al saldo disponible 
opciones incorrectas
entradas no númericas
'''
import time 

def consulta_saldo(saldo):
    print(f"Su saldo es de ${saldo} pesos")
    return saldo

def retirar_dinero(saldo):
    retiro = int(input("Ingrese la cantidad de dinero que desea retirar: "))
    while retiro % 5000 != 0:
        time.sleep(1)
        print("Solo puede retirar multiplos de 5000")
        time.sleep(1)
        retiro = int(input("Ingrese la cantidad de dinero que desea retirar: "))
    while retiro > saldo:
        time.sleep(1)
        print("La cantidad que desea retirar supera su saldo total")
        time.sleep(1)
        retiro = int(input("Ingrese la cantidad de dinero que desea retirar: "))
        if retiro < saldo:
            break
    saldo -= retiro
    print(f"Has retirado ${retiro} pesos")
    return saldo

def depositar_dinero(saldo):
    deposito = int(input("Ingrese la cantidad de dinero que desea ingresar: "))
    while deposito % 5000 != 0:
        time.sleep(1)
        print("Solo puede ingresar multiplos de 5000")
        time.sleep(1)
        deposito = int(input("Ingrese la cantidad de dinero que desea ingresar: "))
    saldo += deposito
    return saldo

saldo_disponible = 100000

while True:
    try:
        op = int(input("Acción a realizar en su cuenta: \n1)Consultar saldo \n2)Retirar dinero \n3)Depositar dinero \n4)Salir \n: "))
        time.sleep(1)
        match op:
            case 1:
                consulta_saldo(saldo_disponible)
                time.sleep(2)
                print("-" * 25)
            case 2:
                saldo_disponible = retirar_dinero(saldo_disponible)
                time.sleep(1)
                print("-" * 25)
            case 3:
                saldo_disponible = depositar_dinero(saldo_disponible)
                time.sleep(1)
                print("-" * 25)
            case 4:
                print("Saliendo de su banca...")
                break
            case _:
                print("Opción inválida")
                time.sleep(1)
                print("-" * 25)

    except ValueError:
        print("-" * 25)
        print("Entrada no númerica")
        print("-" * 25)
        time.sleep(1)

























        