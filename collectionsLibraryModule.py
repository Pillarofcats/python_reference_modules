#COLLECTIONS
def collectionsLibrary():
  from collections import Counter, namedtuple, OrderedDict, defaultdict, deque
  
  print("|| COLLECTIONS LIBRARY ||\n")
  
  str1 = "aaaabbbccd"
  print(f"String: {str1}")
  counter = Counter(str1)
  print(f"Counter creates a dict from a str with each char as a key and a value with the num of char repeats: \n{counter}")
  
  print("")
  
  print(f"Most common element with .most_common(number): \n{counter.most_common(1)}")

  print("")

  print(f"Using Counter method .elements() with list(count.elements()) creates a list: \n{list(counter.elements())}")
  
  print("")