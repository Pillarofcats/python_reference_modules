#LIST COMPREHENSION
def listComprehension():
  print("|| LIST COMPREHENSION ||\n")

  lc1 = [i for i in range(10)]
  print(f"List comprehension 1:\n {lc1}")

  print("")

  lc2 = [[j for j in range(3)] for i in range(5)]
  print(f"List comprehension 2:]\n {lc2}")

  print("")

  lc3 = [i for i in range(10) if i % 2 == 0]
  print(f"List comprehension 3, (Conditional % 2 == 0):\n {lc3}\n")