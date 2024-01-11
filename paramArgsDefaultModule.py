#PARAMATER/ARGUMENT/DEFAULT
# *args / **kwargs
def paramArgsDefault():

  print("|| PARAMATER/ARGUMENT/DEFAULT ||\n")

  def defaultValue(x, y, z=3, ): 
    print(f"Default value:\n x: {x}, y: {y}, default z: {z}")
    return

  defaultValue(y=2, x=1)

  print("")

  def paramArgs(*args): 
    print(f"Dynamic parameters *args:\n (tuple with n arguments) *args : {args}")
    return

  paramArgs(0,1,2,3,4,5,6,7,8,9)

  print("")

  def dynamicFnsKwargs(**kwargs): 
    print(f"Dynamic parameters **kwargs:\n (dictionary with n key/values) **kwargs: {kwargs}")
    print("")
    return

  dynamicFnsKwargs(name="Jacob")
  dynamicFnsKwargs(name="Jacob", age=34)
  dynamicFnsKwargs(name="Jacob", age=34, hobby="Coding")

  def extractArgsKwargs(a, b, c, d): 
    print(f"*args list, **kwargs dict:\n Fn args: (*args) *[1,2], (*kwargs) **{{'c':'three', 'd':'four'}}")
    print(f"a: {a}, b: {b}, c: {c}, d: {d}")
    return

  extractArgsKwargs(*[1,2], **{"c":"three", "d":"four"})

  print("")