#DICT METHODS
def dictMethods():
  print("|| DICT METHODS ||\n")

  aDict = {
    "name": "Jacob",
    "age": 34
  }

  bDict = dict(hobby1="programming", hobby2="cooking" )

  print(f"Dict: {aDict}")
  print(f"Dict['name']: {aDict['name']}")
  print(f"Dict['age']: {aDict['age']}")

  print("")

  print(f"Dict keys: {aDict.keys()}")
  print(f"Dict values: {aDict.values()}")
  print(f"Dict items: {aDict.items()}")

  print("")

  print(f"A Dict: \n{aDict}")
  print(f"B Dict: \n{bDict}")
  aDict.update(bDict)
  print(f"Update A dict with B dict: \n{aDict}")

  print("")

  del aDict['hobby2']
  print(f"Del dict['hobby2']: \n{aDict}")

  print("")

  if 'age' in aDict:
    print(f"If 'age' in aDict: \n{True}")
    
  print("")

  print(f"for key, value in aDict.items():")
  for key, value in aDict.items():
    print(f"{key}: {value}")