#exponente = 0

# print("2 a la potencia " + str(exponente) + " es igual a " +str(2**exponente) )

#-----------------------------------------------------
"""while exponente < 5:
  print("2 a la potencia " + str(exponente) + " es igual a " +str(2**exponente) )
  exponente = exponente + 1"""


"""Buenas practicas
definir una funcion principal"""

#ciclo WHILE
#Definir un límite para el resultado del exponente:

# def run():
#   LIMITE = 1000

#   exponente = 0
#   resultado = 2**exponente
#   while resultado < LIMITE:
#     print(f'2 a la potencia {exponente} es igual a {resultado}' )
#     exponente = exponente + 1
#     resultado = 2 ** exponente



#Ciclo For
from typing import Mapping


def run():
  # for contador in list(range(100)):
  #   print(contador)
  for tabla in range(12):
	  print(f'11 por {tabla} es igual a {11*tabla}')


if __name__== "__main__":   #Funcion principal
  run()
