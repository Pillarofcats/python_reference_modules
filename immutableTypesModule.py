#IMMUTABLE TYPES (copies are NOT referenced, copies don't affect real copy)
def immutableTypes():
  print("|| IMMUTABLE TYPES (PRIMITIVES) ||\n")

  str
  int 
  float
  bool
  bytes
  tuple 

  print(f"str, int, float, bool, bytes, tuple\n")

  iReal = (1,2)
  iCpy = iReal
  iReal = (1,2,3)

  print(f"Note: Changing a copy of an immutable does not affect the original:\n real: {iReal}, cpy: {iCpy}\n")