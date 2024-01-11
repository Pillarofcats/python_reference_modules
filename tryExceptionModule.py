#TRY/EXCEPTION
def tryException():
  print("|| TRY / EXCEPT ||\n")

  try:
    x = int("cat")
    
  except ValueError:
    print ("ValueError: x is not an integer")
    
    print("")