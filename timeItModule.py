#TIMEIT
def timeIt():
  from timeit import default_timer as timer
  
  print("|| TIMEIT ||\n")
  
  start = timer()
  
  for i in range(1000001):
    pass
  
  stop = timer()
  
  print(f"Elapsed time after 1 million loop iterations: {(stop - start):.6f} ms")
  
  print("")