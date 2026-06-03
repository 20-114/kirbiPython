
import random 
import time 


# print(random.randint(1, 10))

# num=random.randint(1, 10)

# for i in range(num):
#     print("wena choro")

# strike=random.randint(10, 70)
# if strike > 50:
#     print("Its a critical hit. Damage ", strike )
# else:
#     print("Its anot very effective. Damage ", strike )

'''
3 personas juegan golf
cada persona tiene la posibilidad de golpear 
y la distancia varia entre 60 y 190
Mostrar al final, el golpe más fuerte
'''
# cont_dist= 0     
    
# for i in range(1, 4):
#     dist = random.randint(60, 190)
#     print(f"El jugador {i} alcanzo una distancia de {dist} metros.")

#     if dist > cont_dist:
#         cont_dist = 0 + dist
#         n = 0 + i

# print(f"El golpe más fuerte fue del jugador {n} con {cont_dist} metros de distancia.")

    
'''
Dos peleadore se piden al inicio de la pelea
Cada peleador inicia con 100 HP
se debe hacer una pelea por turnos
cada golpe varia entre 7 y 18
se ermina el match cuando uno de los 2
tiene su HP menor o igual a 0
Se debe mostrar el ganador al final
Bonus: mostrar la barra de energia de cada peleador.
'''

# p1 = input(f"Ingrese al jugador 1: ")
# p2 = input(f"Ingrese al jugador 2: ")
# # for i in range(1, 3):
# #     p = input(f"Ingrese al jugador {i}")
# hp1 = 100
# hp2 = 100
# turno = random.randint(1, 2)
# while hp1 > 0 or hp2 > 0:
#     golpe = random.randint(16, 25)
#     def critico():
#         crit=random.randint(1, 4)
#         if crit == 2:
#             golpe = golpe * 1.4
#     if turno % 2 == 0:
#         print(f"Turno de {p1} ")
#         critico()
#         hp1 -= golpe
#         print(f"Golpeo con {golpe} puntos de daño.")
#         print(f"El jugador {p2} tiene {hp2} HP")
#         time.sleep(1)
#         print(f"***********************************")
#     else:
#         print(f"Turno de {p2} ")
#         critico()
#         hp2 -= golpe
#         print(f"Golpeo con {golpe} puntos de daño.")
#         print(f"El jugador {p1} tiene {hp1} HP")
#         time.sleep(1)
#         print(f"***********************************")
#     turno += 1
#     h = "-"
#     print(f"{p1}: {h * hp1} ")
#     print(f"{p2}: {h * hp2} ")
# if hp1 > hp2:
#     print(f"El jugador {p1} es el ganador del combate")
# else:
#     print(f"El jugador {p2} es el ganador del combate")

'''
Crea un númer random entre 1 y 100
Pide al usuario que adivine el número
Si el usuario pone un número mayor al generado
debe decir "Te pasate", en caso contrario
"El número a adivinar es mayor"
Solo hay 5 posibilidades de adivinar
'''

num = random.randint(1, 10)
pos = 1
user = int(input(f"Adivina el número: "))
while user < 1 or user > 100:
    print("Número fuera de rango, intente nuevamente")
    user = int(input(f"Adivina el número: "))
while user != num and pos < 5:
    if user > num:
        print("Te pasaste")
    elif user < num :
        print("El número a adivinar es mayor")
    user = int(input(f"Adivina el número: "))
    while user < 1 or user > 100:
        print("Número fuera de rango, intente nuevamente")
        user = int(input(f"Adivina el número: "))
    pos += 1

if user == num:
    print("Has adivinado")
else:
    print("Se te acabaron las oportunidades")