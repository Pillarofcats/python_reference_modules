#CLASS MAGIC METHODS
def classMagicMethods():
  print("|| CLASS MAGIC METHODS ||\n")

  class Cat:
    color = "black"
    age = 3
    
    def __init__(self, name) -> None:
      self.name = name
      
    def __str__(self) -> str:
      return f"{{name: {self.name}, color: {self.color}, age: {self.age}}}"

    def __repr__(self) -> str:
      return f"type: {type(self)}, \n\tsize: {self.__sizeof__() } bytes, \n\tinstance attr: {self.__dict__}, \n\tclass attr: {{'color': '{self.color}', 'age': '{self.age}'}}"
      
  cat = Cat("Vader")

  print(f"Creating Cat class instance: \n\tcat = Cat('Vader')")
  print(f"__init__: \n\tInstantiate constructor instance attribute -> self.name = 'Vader'")
  print(f"__str__: \n\t{cat.__str__()}")
  print(f"__repr__: \n\t{cat.__repr__()}")

  print("")