def cambio_monedas(pais_pesos, cambio_dolar):
    pesos = input("Cuántos pesos " + pais_pesos + " tienes: ")
    pesos = float(pesos)
    dolares = pesos / cambio_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("El dinero que tienes en dólares es de " + dolares)

menu = """
Bienvenido al conversor de monedas 💛💹

1- Pesos colombianos
2- Pesos argentinos
3- pesos peruanos

Elige un opción: 
"""

opcion = input(menu)

if opcion == "1":
    cambio_monedas("argentinos", 3528)
elif opcion == "2":
    cambio_monedas("colombianos", 654)
elif opcion == "3":
    cambio_monedas("mexicanos", 528)
else:
    print("Escribe una opción correcta")

