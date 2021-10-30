menu = """
Bienvenido al conversor de monedas 💛💹

1- Pesos colombianos
2- Pesos argentinos
3- pesos peruanos

Elige un opción: 
"""

opcion = input(menu)

if opcion == "1":
    pesos = input("Escribe el dinero que tienes en pesos argentinos: ")
    pesos = float(pesos)
    cambio_dolar = 24
    dolares = pesos / cambio_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("El dinero que tienes en dólares es de " + dolares)
elif opcion == "2":
    pesos = input("Escribe el dinero que tienes en pesos argentinos: ")
    pesos = float(pesos)
    cambio_dolar = 65
    dolares = pesos / cambio_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("El dinero que tienes en dólares es de " + dolares)
elif opcion == "3":
    pesos = input("Escribe el dinero que tienes en pesos: ")
    pesos = float(pesos)
    cambio_dolar = 3.95
    dolares = pesos / cambio_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("El dinero que tienes en dólares es de " + dolares)
else:
    print("Escribe una opción correcta")

