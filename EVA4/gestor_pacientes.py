'''crear al gestor de pacientes en un centro medico

Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres

Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa

Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''

pacientes=[

  {"nombre": " Aquiles Baeza", 
   "prevision": "Fonasa", 
   "temperatura":34.6, 
   "grave": False}
]

def ingreso_temp(temperatura):
    if temperatura > 39:
        return True
    else:
        return False

def gravedad(tempe):
    if tempe:
        return "GRAVE"
    else:
        return "NORMAL"
    

valor_atencion = 25000
Fonasa = 0.46
Isapre = 0.73
Fodesa = 0.875

while True:
    try:
        while True:
            print("-"*30)
            nombre = input("Ingresa el nombre del paciente \n : ")
            if not nombre:
                print("No puede dejar el campo en blanco")
                continue
            elif len(nombre) < 8:
                print("El nombre debe contener almenos 8 caracteres")
                continue
            break
        while True:
            print("-"*30)
            try:
                temp = float(input("Indique la temperatura del paciente \n : "))
                if not temp:
                    print("No puede dejar el campo en blanco")
                    continue
                if temp < 0:
                    print("Solo puede ingrese números positivos")
                    continue
            except ValueError:
                print("Solo puede ingrese números positivos")
                continue
            temp_ingreso = ingreso_temp(temp)
            break
        while True:
            print("-"*30)
            print("PREVISIONES \n1. Fonasa \n2. Isapre \n3. Fodesa")
            prevision = input("Indique la previsión del paciente \n : ")
            match prevision:
                case "1":
                    total = valor_atencion * Fonasa
                    break
                case "2":
                    total = valor_atencion * Isapre
                    break
                case "3":
                    total = valor_atencion * Fodesa
                    break
                case _:
                    print("Ingreso Inválido")
                    continue

        pacientes.append({
            "nombre": nombre, 
        "prevision": prevision, 
        "temperatura":temp, 
        "grave": temp_ingreso})

        print("-"*30)
        for pac in pacientes:
            print(f"Paciente : {pac['nombre']} | Temperatura : {pac['temperatura']}° | Previsión : {pac['prevision']} | Estado {gravedad(temp_ingreso)} según su temperatura")
            
    except KeyboardInterrupt:
        print("Sistema caido...")
        break


