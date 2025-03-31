#Programa que recorre una lista de cadenas y elimina los espacios en blanco al principio y final de una cadena

cadena = [" Hola ", " Mundo ", " Ayuda "]
cadenamodificada = []

for i in cadena:
    nelemento = i.strip()
    cadenamodificada.append(nelemento)

print(cadenamodificada)