#Programa que recorre una lsita de cadenas y divide cada cadena en subcadenas utilizando un delimitador

lista = ["La UAM", "Es la mejor", "Universidad de Managua"]
nueva_lista = []

for string in lista:
    subcadenas = string.split(" ")
    nueva_lista.append(subcadenas)

print(nueva_lista)