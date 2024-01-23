def shallowCopy():
  print("|| COPY LIST BY VALUE, SHALLOW COPY ||\n")

  #Copy mutable list, shallow by value using list() consructor
  aList = [1,2,3,4,5]
  cpyAList = list(aList)

  print(f"Note: Copy mutable list by value using list()\n list: {aList}, list copy: {cpyAList}\n")
  
  print("")