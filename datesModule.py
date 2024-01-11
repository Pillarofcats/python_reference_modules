#DATES
def dates(): 
  print("|| DATES ||\n")

  import datetime

  d1 = datetime.datetime.now()
  d2 = datetime.date.today()
  d3 = datetime.time.max
  d4 = datetime.timezone.utc

  print(f"datetime.now(): {d1}")
  print(f"date.today(): {d2}")
  print(f"time.max: {d3}")
  print(f"timezone.utc: {d4}")

  print("")