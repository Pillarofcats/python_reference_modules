#PARSE JSON
def parseJSON():
  print("|| CONVERT JSON / PARSE JSON ||\n")

  import json

  j = { 
    "name": "Jacob",
    "age": 34  
  }

  convertToJSON = json.dumps(j)
  print(f"Dict converted to JSON String using: json.dumps(Dict Object) {type(convertToJSON)}")
  parseToJSON = json.loads(convertToJSON)
  print(f"JSON parsed to Dict using: json.loads(JSON String) {type(parseToJSON)}")

  print("")

  #PARSE JSON
  print("|| PIP (PACKAGE MANAGER) ||\n")

  print(f"PIP version: pip --version")
  print(f"PIP install: pip install packageName")
  print(f"PIP uninstall: pip uninstall packageName")
  print(f"PIP list packages: pip list")

  print("")