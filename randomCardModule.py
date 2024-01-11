def randomCard():
  #IMPORT RANDOM
  print("|| RANDOM ||\n")

  import random
  cards = ["Jack", "Queen", "King", "Ace"]
  print(f"cards:\n { cards }")
  random.shuffle(cards)
  print(f"shuffled cards:\n{ cards }")
  print("")