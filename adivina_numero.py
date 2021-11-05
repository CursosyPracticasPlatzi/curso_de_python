import random


def run():
  numero_aletorio = random.randint(1,100)
  numero_elegido = int(input("Escribe un numero del 1 al 100: "))
  while numero_elegido != numero_aletorio:
    if numero_elegido < numero_aletorio:
      print("Escribe un número mayor")
    else:
      print("Escribe un número menor")
    numero_elegido = int(input("Escribe otro número: "))
  print("¡Ganaste!")


if __name__ == "__main__":
  run()