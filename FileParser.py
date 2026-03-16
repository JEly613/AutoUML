import re

# Parser that handles a single class file
class FileParser:
    def __init__(self, filePath):
        self.className = _readValues()['name']
        self.classVars = _readValues()['vars']
        self.classMethods = _readValues()('methods')

def printClass():
    # print class header
    print("class ", self.className, " {")

    # print instance variables
    for var in self.classVars:
        print(str(var))

    # print methods
    for method in self.classMethods:
        print(str(method))

    # closing bracket
    print("}")
    
'''
TODO:
printClass, prints class in plantuml format
_readValues, reads file for class name, instance variables, methods
'''