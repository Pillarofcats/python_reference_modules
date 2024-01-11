#ITERATORS
def iterators():
  print("|| ITERATORS ||\n")

  numList = [1,2,3]
  numListIter = iter(numList)

  try:  
    print(f"Iteration: {next(numListIter, 'end')}")
    print(f"Iteration: {next(numListIter, 'end')}")
    print(f"Iteration: {next(numListIter, 'end')}")
    #Out of range, error on next iteration
    print(f"Iteration: {next(numListIter, 'end')}")

  except ValueError:
    print(f"ValueError: Iterator out of bounds")
    
  print("")
    
  class ListIter:

    def __init__(self, aList):
      self.aList = aList

    def __iter__(self):
      self.ind = 0
      return self

    def __next__(self):
      if self.ind < len(self.aList):
        val = self.aList[self.ind]
        self.ind += 1
        return val
      
      else:
        raise StopIteration

  listIter = ListIter(["a","b","c"])
  iterable = iter(listIter)

  print(f"Custom class iteration: {next(iterable, 'end')}")
  print(f"Custom class iteration: {next(iterable, 'end')}")
  print(f"Custom class iteration: {next(iterable, 'end')}")
  print(f"Custom class iteration: {next(iterable, 'end')}")

  print("")