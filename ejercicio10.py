lista = ["Hola", "Mundo", "Tengo", "Sueñoo"]

for string in lista:
    x = string.upper()
    conteo = x.count("O")
    print(f"El caracter 'o' aparece {conteo} veces en la cadena")