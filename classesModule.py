#CLASSES
def classes():
  print("|| CLASSES ||\n")

  class Job:
    #Constructor on a child class will not inherit parent's constructor
    hasJob = True
    
    def sayJob(self):
      return f"I am a professional {self.job}"
      
    #String representation of object  
    def __str__(self):
      return f"{{'job': {self.job} }}"
    
  class CarOwner:
    #Constructor on a child class will not inherit parent's constructor
    hasCar = True

  class Person(Job, CarOwner):
    #Constructor/Initial
    def __init__(self, name, age, job, car):
      #Inherit methods/properties from (class Job & class CarOwner)
      super().__init__()
      #OR inherit methods/properties WITH:
      # Job.__init__()
      # CarOwner.__init__()
      
      #properties
      self.name = name
      self.age = age
      self.job = job
      self.car = car
      
    #String representation of object  
    def __str__(self):
      return f"{{'name': {self.name}, 'age': {self.age}, 'job': {self.job}, 'car': {self.car}}}"
    

  jacob = Person("Jacob", 34, "Developer", "Ford Focus")

  print(f"Person class object: {jacob}")
  print(f"Person class object name: {jacob.name}")
  print(f"Person class object age: {jacob.age}")
  print(f"Person class object inherited CarOwner class: {jacob.car}")
  print(f"Person class object inherited property hasCar class: {jacob.hasCar}")
  print(f"Person class object inherited Job class: {jacob.job}")
  print(f"Person class object inherited property hasJob: {jacob.hasJob}")
  print(f"Person class object inherited method sayJob: {jacob.sayJob()}")

  print("")