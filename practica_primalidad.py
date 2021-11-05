def es_primo(numero):
  for i in range(2, numero):
    if numero % i == 0:
      return True
    else:
      return False


def run():
  numero = int(input("Escribe un numero: "))
  if es_primo(numero):
    print("No es primo")
  else:
    print("Es primo")


if __name__ == "__main__":
  run()