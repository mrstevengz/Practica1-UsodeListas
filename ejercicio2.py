#Programa que recorra una lista de cadenas y calcule la longitud, almacenando el resultado en otra lista

cadena = ["Hola", "123", "Duran", "Mejor", "Maestro"]
longitud = []

for i in cadena:
    longitud.append(len(i))

print(longitud)