#WRITE FILES / READ FILES
def writeReadFiles():
  print("|| WRITE FILES / READ FILES ||\n")

  fw = open("aFile.txt", "w+t")

  print(f"Writing to file:")
  for i in range(1,6):
    print(f"Line {i}")
    fw.write(f"Line {i}\n")

  fw.close()

  print("")

  fr = open("aFile.txt","r+t")
  read = fr.read()
  print(f"Reading file: \n{read}")

  fr.close()