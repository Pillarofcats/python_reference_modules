#IMPORT MODULES
def importAdd(x, y):
  
  if(not(isinstance(x, str) & isinstance(y, str) | isinstance(x, int) & isinstance(y, int)) ):
    print(f"Error, wrong data type")
    return None
  
  if(isinstance(x, str) & isinstance(y, str)):
    return int(x) + int(y)
  
  return x + y

#WHEN RUNNING MODULE INDEPENDENTLY (AS SCRIPT), CLI: python addModule.py 2 3
if __name__ == "__main__":
  import sys
  print("Running module directly as __main__")
  
  print(f"Adding {sys.argv[1]} + {sys.argv[2]} = { importAdd(sys.argv[1], sys.argv[2]) }")
  