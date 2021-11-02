# def run():
#   for contador in range(100):
#     # if contador % 2 != 0:
#     #   continue
#     # print(contador)
#     print(contador)
#     if contador == 59:
#       break


# if __name__ == "__main__":
#   run()

def run():
  frase = "Bendito seas Señor Jesús, no me desampares"
  for i in frase:
    if i == "n":
      continue
    if i == "p":
      break
    print(list(i))


if __name__ == "__main__":
  run()