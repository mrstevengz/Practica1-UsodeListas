#Programa que busca si una subcadena esta presente en cada una de las cadenas de una lista. Luego devuelve un booleano que indican si fue encontrada o no

lista = ["Hola mundo", "Hola clase", "Python"] 
nuevacadena = []  

for cadena in lista:
    nuevacadena.append("Hola" in cadena) 

print(nuevacadena)