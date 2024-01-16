#SET METHODS
def setMethods():
  print("|| SET METHODS ||\n")
  
  aSet = {2,1,3,4,5}
  bSet = set({9,7,8,10,12})
  cSet = {13}
  dSet = {1,3,4,11}
  eSet = {1}
  fSet = {42}
  gSet = frozenset({1,2,3,4})

  print(f"Set a: \n{aSet}")
  print("")

  print(f"Set b: \n{bSet}")
  print("")

  aSet.add(6)

  print(f"Set a add 6: \n{aSet}")
  print("")

  aSet.remove(2)

  print(f"Set a remove 2: \n{aSet}")
  print("")

  aSet.discard(11)

  print(f"Set a discard 11, no error: \n{aSet}")
  print("")

  aSet.update(cSet)
  print(f"Set a: \n{aSet}")
  print(f"Set c: \n{cSet}")
  print(f"Set update a & c: \n{aSet}")
  print("")

  print(f"Set a: \n{aSet}")
  print(f"Set b: \n{bSet}")
  print(f"Set union merge a & c, returns new set: \n{aSet.union(bSet)}")
  print(f"Set a unchanged from a & b union: \n{aSet}")
  print("")

  print(f"Set a: \n{aSet}")
  print(f"Set d: \n{dSet}")
  print(f"Set a & d intersection, returns all shared values: \n{aSet.intersection(dSet)}")
  print(f"Set d & a difference, returns set d non-shared values: \n{dSet.difference(aSet)}")
  print(f"Set a & d difference, returns set a non-shared values: \n{aSet.difference(dSet)}")
  print(f"Set a & d symmetric difference, returns all non-shared values: \n{aSet.symmetric_difference(dSet)}")
  print("")

  print(f"Set a: \n{aSet}")
  print(f"Set e: \n{eSet}")
  print(f"Set e & a issubset, returns True if set e issubset of set a: \n{eSet.issubset(aSet)}")
  print(f"Set a & e issuperset, returns True if set a issuperset of set e: \n{aSet.issuperset(eSet)}")
  print("")

  print(f"Set a: \n{aSet}")
  print(f"Set f: \n{fSet}")
  print(f"Set a & f isdisjoint, returns True if set a isdisjoint of set f: \n{aSet.isdisjoint(fSet)}")
  print("")
  
  print(f"Frozenset g: \n{gSet}")
  print(f":Frozenset g cannot be mutated after creation: \n{gSet}")
  print("")
