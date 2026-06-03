#run time = tiempo de ejecución -> programa recursivo

for i in range(1,12):
    cont = 1
    num = 8
    while cont <= 12:
        mult = num * cont
        print(f"{num} x {cont} = {mult}")
        cont += 1



##codigo secreto
code = 1234

pwd=int(input("Ingrese el pin"))

while code != pwd:
    print("Clave invalida, intente de nuevo")
print("Acceso correcto")