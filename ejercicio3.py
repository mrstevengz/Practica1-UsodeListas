#Programa que recorra una lista de cadenas, y convierta cada cadena a mayuscula o minuscula dependiendo si es par o inpar

lista = ["ABCD", "DEF", "GHIJ", "KLM"]
longitud = 0

for i in lista:
    longitud = len(i)
    if longitud % 2 == 0:
        print(i.upper())
    else:
        print(i.lower())
