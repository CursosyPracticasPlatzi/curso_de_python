def cambiar_palabra(frase):
  palabra = ""
  for letter in frase:
    if letter == letter.upper():
      palabra += letter.lower()
    else:
      palabra += letter.upper()
  return palabra


def run():
  palabra = input("Escribe una palabra: ")
  resultado = cambiar_palabra(palabra)
  print(resultado)

if __name__ == "__main__":
  run()