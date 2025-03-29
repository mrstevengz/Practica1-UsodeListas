#Programa que recorra una lista de cadenas y reemplace todas las apariciones de un carácter específico con otro carácter, y luego las imprima en una lista

lista = ["Hola", "mundo", "odio", "sistemas"]
nlista = []


for k in lista:
    nstring = k.replace("a", "b")
    nlista.append(nstring)

print(nlista)
    

