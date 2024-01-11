#LIST METHODS
def listMethods():
  print("|| LIST METHODS ||\n")

  aList = ["Jacob", "Dan", "Michael"]
  print(f"List: {aList}")

  aList.insert(1, "Bayleigh")
  print(f"List insert 'Bayleigh' at index 1: {aList}")

  aList.append("Erik")
  print(f"List append 'Erik': {aList}")

  if "Jacob" in aList:
    print(f"Jacob is in the list.")
    
  print(f"Last name in list: {aList[-1]}")

  aList.remove("Dan")
  print(f"Remove 'Dan' from list: {aList}")

  aList.reverse()
  print(f"Reverse list: {aList}")

  #mutated sort
  aList.sort()
  print(f"Sorted list (mutated): {aList}")

  print(f"Sliced list 1-4: {aList[1:3]}")

  print("")