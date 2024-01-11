#IMPORT TIMEIT
def importTimeIt():
  print("|| IMPORT TIMEIT ||\n")

  import timeit

  l = timeit.timeit(stmt="[0,1,2,3]", number=1000000)
  t = timeit.timeit(stmt="(0,1,2,3)", number=1000000)

  print(f"List instantiation [0,1,2,3]: {l}")
  print(f"Tuple instantiation (0,1,2,3): {t}")
  print(f"Tuple is faster than a List.")

  print("")