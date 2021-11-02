#Recorrer las letras de una frase o palabra

def run():
  frase = input('Escribe una frase: ')
  for letra in frase:
    print(letra.upper())


if __name__ == "__main__":
  run()