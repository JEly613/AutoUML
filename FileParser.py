import re

# Parser that handles a single class file
class FileParser:
    def __init__(self, filePath):
        self.className = _readValues()['name']
        self.classVars = _readValues['vars']
        self.classMethods = _readValues['methods']

'''
TODO:
printClass, prints class in plantuml format
_readValues, reads file for class name, instance variables, methods
'''