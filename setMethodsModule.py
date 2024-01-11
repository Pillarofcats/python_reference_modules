#SET METHODS
def setMethods():
  print("|| SET METHODS ||\n")
  
  aSet = {1,2,3,4,5}
  bSet = {7,8,9,10}
  
  print(f"Set a: {aSet}")
  print(f"Set b: {bSet}")
  
  aSet.add(6)
  
  print(f"Set add: {aSet}")
  
  aSet.update(bSet)
  
  print(f"Set update: {aSet}")
  print("")
