# File Name: Employee.py
# Developer: Christopher Cox
# Date last modified: 12/11/2017
# Description: The file contains the base class named Employee.
#     This class will be used to hold an em.'s name and ID #
#
# E-Mail: thetaco.dyndns@gmail.com

class Employee:

    # Class variables
    _name = None
    _ID = 0

    # Constructor
    def __init__(self, name, ID):

        self._name = name
        self._ID = ID
    
    # Accessors and modifiers
    def getName(self):
        return self._name

    def setName(self, name=None):
        self._name = name

    def getID(self):
        return self._ID

    def setID(self, ID=0):
        self._ID = ID

    # End Employee class

# Make sure this is only imported
if (__name__ == "__main__"):
    print("This file is only to be imported as a module!")
    quit()
