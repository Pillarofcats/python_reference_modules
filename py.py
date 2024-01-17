#IMMUTABLE TYPES (copies are NOT referenced, copies don't affect real copy)
from immutableTypesModule import immutableTypes
immutableTypes()

#MUTABLE TYPES (copies are referenced, copies affect real copy)
from mutableTypesModule import mutableTypes
mutableTypes()

#SHALLOW COPY
from shallowCopyModule import shallowCopy
shallowCopy()

#LIST COMPREHENSION
from listComprehensionModule import listComprehension
listComprehension()

#PARAMATER/ARGUMENT/DEFAULT
# *args / **kwargs
from paramArgsDefaultModule import paramArgsDefault
paramArgsDefault()

#IMPORT MODULES
print("|| IMPORT MODULES ||\n")
from importAddModule import importAdd
#from (module file) import (module function/variables/etc)
print(f"from importAddModule import importAdd] \nAdding 1 + 2 with ImportAddModule Fn importAdd(1,2): { importAdd(1,2) }")

print("")

#GLOBAL INTERPRETER LOCK (GIL) PYTHON ONLY RUNS 1 THREAD AT A TIME
#NOT MULTITHREADED
from gilModule import gil
gil()

#TRY/EXCEPTION
from tryExceptionModule import tryException
tryException()

#IMPORT RANDOM
from randomCardModule import randomCard
randomCard()

#TUPLE METHODS
from tupleMethodsModule import tupleMethods
tupleMethods()

#LIST METHODS
from listMethodsModule import listMethods
listMethods()

#SET METHODS
from setMethodsModule import setMethods
setMethods()

#DICT METHODS
from dictMethodsModule import dictMethods
dictMethods()

#FOR LOOPS
from forLoopsModule import forLoops
forLoops()

#CLASSES
from classesModule import classes
classes()

#ITERATORS
from iteratorsModule import iterators
iterators()

#POLYMORPHISM
from polymorphismModule import polymorphism
polymorphism()

#DATES
from datesModule import dates
dates()

#PARSE JSON
from parseJSONModule import parseJSON
parseJSON()

#PIP PACKAGE MANAGER
from pipModule import pip
pip()

#USER INPUT
from userInputModule import userInput
userInput()

#WRITE FILES / READ FILES
from writeReadFilesModule import writeReadFiles
writeReadFiles()

#CLASS MAGIC METHODS
from classMagicMethodsModule import classMagicMethods
classMagicMethods()

#IMPORT TIMEIT
from importTimeItModule import importTimeIt
importTimeIt()

#STRINGS
from stringsModule import strings
strings()

