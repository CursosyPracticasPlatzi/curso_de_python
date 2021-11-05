"""Vamos a ver si un numero es primo o no mediante un código

  un numero primo es uno que solo se puede dividir entre 1 y su mismo numero.
  Vamos a ver si el numero es divisible por otros numero diferentes a 1 y al
  mismo numero; si es así, ese numero no es primo, de lo contrario, es primo"""


#1) Primero la función principal de inicio
def es_primo(numero):                         #3) desarrollamos la función ejecutadora
  contador = 0
  for i in range(1,numero+1):
    if numero % i != 0:
      continue
    else:
      contador += 1
  if contador == 2:
    return True
  else:
    return False
#!Un nuevo código que funciona!


def run():
  numero = int(input("Escribe el numero: "))
  if es_primo(numero):                        #2) identificamos la funcion que va a accionar el resultado: si es primo o no es primo
    print("Es un número primo")
  else:
    print("No es un número primo")


if __name__ == "__main__":
  run()



#Pasos para escribir en python:
#1) función principal de inicio __name__
#2) función de definicion- se encarga de dar la respuesta, pero no la ejecuta
#3) funcion ejecutadora- se encarga de ejecutar la operacion, el resultado lo envía a la función de definición.