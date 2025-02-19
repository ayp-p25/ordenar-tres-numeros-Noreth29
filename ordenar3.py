"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Declaraciones


# Entradas
E1 = int(input("Primer número: "))
E2 = int(input("Segundo número: "))
E3 = int(input("Tercer número: "))

# Proceso
if E1 != E2 and E1 != E3 and E2 != E3:

    if E1 > E2 and E2 > E3:
        salida = str(E1) + " " + str(E2) + " " + str(E3)
    if E1 > E3 and E3 > E2:
        salida = str(E1) + " " + str(E3) + " " + str(E2)

    if E2 > E3 and E3 > E1:
        salida = str(E2) + " " + str(E3) + " " + str(E1)
    if E2 > E1 and E1 > E3:
        salida = str(E2) + " " + str(E1) + " " + str(E3)

    if E3 > E1 and E1 > E2:
        salida = str(E3) + " " + str(E1) + " " + str(E2)
    if E3 > E2 and E2 > E1:
        salida = str(E3) + " " + str(E2) + " " + str(E1)

    print("Números ordenados: " + str(salida))   

else:
    no = "Error. Por favor, escribe números diferentes."

    print(no)
