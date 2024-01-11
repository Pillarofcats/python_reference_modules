#USER INPUT
def userInput():
  print("|| USER INPUT ||\n")

  try:
    inp = int(input("What is your name? (Forcing an error): "))
    print(f"The user's name is: {inp}")
  except ValueError as e:
    print(f"Input type not a String. {e}")
    
  print("")