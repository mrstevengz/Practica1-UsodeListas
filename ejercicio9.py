#Programa que recorre cadenas y elimina las que estan vacias

lista = ["Son", "Las", "2am", "", "Ayuda", ""]
nlista = []

for string in lista:
    if string:
        nlista.append(string)

print(nlista)
