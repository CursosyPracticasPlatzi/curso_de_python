import random


def generar_contrasena():
  mayusculas = ['A','B','C','D','E','F','G']
  minusculas = ['a','b','c','d','e','f','g']
  simbolos = ['@','#','$','%','&']
  numeros = ['1','2','3','4','5','6','7','8','9','0']

  caracteres = mayusculas + minusculas + simbolos + numeros

  contrasena = []

  for i in range(15):
    random_caracter = random.choice(caracteres)
    contrasena.append(random_caracter)           #Hasta aquí ya hemos llevado los 15 caracteres a la lista contraseña.

  contrasena = "".join(contrasena)                #Aquí cambiamos los valores de la lista en letras juntas.
  return contrasena                               #Retornamos la contraseña de 15 digitos aleatoriamente.

def run():
  contrasena = generar_contrasena()
  print("Tu contraseña es", contrasena)


if __name__ == "__main__":
  run()