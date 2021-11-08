def run():
  mi_diccionario = {
    "llave1" : 1,
    "llave2" : 2,
    "llave3" : 3,
  }

  # print(mi_diccionario["llave1"])
  # print(mi_diccionario["llave2"])
  # print(mi_diccionario["llave3"])
  # print(mi_diccionario)

  # for llave in mi_diccionario:
  #   print(llave)

  # for llave in mi_diccionario.keys():
  #   print(llave)

  # for llave in mi_diccionario.values():
    # print(llave)

  for llave, valor in mi_diccionario.items():
    print("En esta", llave, "está el valor", valor)
    print("En esta " + llave + " está el valor " + str(valor))
    print(f'En esta {llave} está el valor {valor}')


if __name__ == "__main__":
  run()