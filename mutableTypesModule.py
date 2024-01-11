#MUTABLE TYPES (copies are referenced, copies affect real copy)
def mutableTypes():
  print("|| MUTABLE TYPES (OBJECTS) ||\n")

  list
  set
  dict

  print(f"list, set, dict\n")

  mReal = [1,2]
  mCpy = mReal
  mReal[1] = 1

  print(f"Note: Changing a copy of a mutable affects the original:\n real: {mReal}, cpy: {mCpy}\n")