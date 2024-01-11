#POLYMORPHISM
def polymorphism():
  print("|| POLYMORPHISM (many forms) ||\n")

  class Animal:
    isAlive = True
    aType = "mammal"
    
    def talk():
      return f"animal talk"

  class Dog:
    legs = 8
    
    def talk():
      return f"dog talk"
    
  class Cat(Animal):
    legs: 4

  cAnimal = Animal
  cDog = Dog
  cCat = Cat

  print(f"Class Animal with method talk(): {cAnimal.talk()}")
  print(f"Class Dog with method talk(): {cDog.talk()}")
  print(f"Class Cat WITHOUT method talk() inherited Animal class method talk(): {cCat.talk()}")

  print("")