
entrenador = "jesi"
pkm1 = 6

entrenador2 = "Sabrina"
pkm2 = 7

# if pkm2 <= 6:
#     print("Puede acceder a la liga Pokemon")
# else:
#     print("Tiene más Pokemons de los necesarios")

# print(len(entrenador))

# print("El entrenador ", entrenador, " tiene ", pkm1, "  pokemons")
# print("El entrenador ", entrenador2, " tiene ", pkm2, "  pokemons")
# print("El entrenador "+ entrenador2+ " tiene "+ pkm2+ "  pokemons")
# print(f"El entrenador {entrenador2} tiene {pkm2} pokemons")

# print(f"Hola {entrenador} " * 4)

# print(entrenador[0])

'''
Pedir la lcave al usuario
y verificar que sea SHAZAM
(independiente de mayuscula o minuscula)
'''

# passw = "SHAZAM"

# usuario = input("Ingresar usuario: ")
# cont = (input("Ingresar contraseña: "))

# if passw == cont.upper():
#     print("Acceso permitido")
# else:
#     print("contraseña invalida")

'''
Crear un nombre de usuario y verificar
que su largo esté entre 4 y 10 caracteres
'''

# newUser = input("Cree su nombre de usuario: ")

# if len(newUser) >= 4 and len(newUser) <= 10:
#     print("Usuario creado corectamente")
# else:
#     print("Su usuario no comple con 4 caracteres minimos y 10 maximos")

# if len(newUser) < 4:
#     print("Usuario con menos de 4 caracteres")
# elif len(newUser) > 10:
#     print("Usuario con más de 10 caracteres")
# else:
#     print("Usuario creado correctamente")

'''
Crear un pin y que este 
tenga exactamente 4 digitos
'''

pin = input("Cree su pin con 4 digitos: ")

if len(pin) == 4:
    print("Pin creado corectamente")
    pinn = int(pin)
else:
    print("Su pin no cumple con los 4 digitos")
