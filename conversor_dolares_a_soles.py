dolares = input("Cuántos dólares tienes: ")
dolares = float(dolares)
cambio_soles = 3.95
soles = dolares * cambio_soles
soles = round(soles, 2)
soles = str(soles)

print("Tú tienes en soles la cantidad de " + soles)