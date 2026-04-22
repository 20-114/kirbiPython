# op = 0
# while op != 4:
#     uno = 70000
#     dos= 500000
#     tres = 580000
#     iva = 1.19
#     total = 0
#     print(f"1. Radio estereo SONY {uno}\n2. LGTV 55 pulgadas Super gamer {dos} \n3. PS5 {tres} \n4. Salir")
#     op = int(input("Seleccione una opción "))
#     match op:
#         case 1:
#             print(f"El precio a pagar es  {uno * iva}")
#             total += (uno * iva)
#             print("----------------------------")
#         case 2:
#             print("El precio a pagar es ", dos * iva)
#             total += dos * iva
#             print("----------------------------")
#         case 3:
#             print("El precio a pagar es ", tres * iva)
#             total += tres * iva
#             print("----------------------------")
#         case 4:
#             print(f"Total a pagar es {total}")
#             print("----------------------------")
#         case _:
#             print("Opción Inválidad") #opción por defecto

def calculadora():
    def suma():
        print("Ingrese dos números para sumar")
        n1 = int(input("primer número "))
        n2 = int(input("segundo número "))
        suma = n1 + n2
        print("El resultado es ", suma)
        print("--------------------------")
    def resta():
        print("Ingrese dos números para restar")
        n1 = int(input("primer número "))
        n2 = int(input("segundo número "))
        res = n1-n2
        print(f"El resultado es {res}")
        print("--------------------------")
    def mult():
        print("Ingrese dos números para multiplicar")
        n1 = int(input("primer número "))
        n2 = int(input("segundo número "))
        mul = n1*n2
        print(f"El resultado es {mul}")
        print("--------------------------")
    def div():
        print("Ingrese dos números para dividir")
        n1 = int(input("primer número "))
        n2 = int(input("segundo número "))
        div = n1/n2
        print(f"El resultado es {div}")
        print("--------------------------")

    op = 0
    while op != 5:
        op = int(input("Operaciones: \n1. Suma \n2. Resta \n3. Multiplicación \n4. División \n5. Salir \nSeleccione una opción " ))
        match op:
            case 1:
                suma()
            case 2:
                resta()
            case 3:
                mult()
            case 4:
                div()
            case 5:
                print("Saliendo del sistema")
            case _:
                print("Ingreso invalido")
                print("--------------------------")
def prom_notas():
    print("CALCULO DE PROMEDIO")
    print("Ingrese tres notas")
    n1 = int(input("primera nota "))
    n2 = int(input("segunda nota "))
    n3 = int(input("tercera nota "))
    prom = (n1 + n2 + n3) / 3
    print("El promedio es: ", prom)
    if prom > 3.9:
        print("APROBADO")
    else:
        print("REPROBADO")
    print("------------------------------")
def boletos():
    nom = int("Ingrese su nombre ")
    edad = int("Ingrese su edad ")
    

op = 0
while op != 4:
    op = int(input(f'''
PROGRAMAS:
1. Promedio de notas
2. Calculadora
3. Programa 3
4. Salir
Seleccione un programa: '''))
    match op:
        case 1:
            calculadora()
        case 2:
            prom_notas()
        case 3:
            print("hola")
        case 4:
            print("Saliendo")
        case _:
            print("Ingeso invalido")

# name = "Carlos"
# def saludo():
#     print("Hola, ¿como van?")

# saludo

# def chao():
#     print(f"Ya nos vamos {name}")

# chao

