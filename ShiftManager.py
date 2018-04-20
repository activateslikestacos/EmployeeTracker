# File Name: ShiftManager.py
# Developer: Christopher Cox
# Date last modified: 12/12/2017
# Description: A script holding the ShiftManager class. The shift manager
#     class is for keeping track of all employees easily.
#
# E-Mail: thetaco.dyndns@gmail.com

from ProductionWorker import ProductionWorker

# Create the class (No inheritance needed)
class ShiftManager:

    # Create class variables
    productionWorkers = None

    # Constructor
    def __init__(self):

        self.productionWorkers = {}

    # Accessors and modifiers
    def addPW(self, emp):

        # Store employee in dictionary using their ID as the key
        self.productionWorkers[emp.getID()] = emp

    def getPWs(self):

        return self.productionWorkers
    
    # A 'private' function for printing a single employee
    def _printPW(self, emp):
        
        nameCombo = str(emp.getID()) + ': ' + emp.getName()
        nameSize = len(nameCombo)

        # Perform some basic math to match up the text with the header
        shiftOffset = 26 - nameSize
        payRateOffset = nameSize + shiftOffset - 11
        hourOffset = nameSize + shiftOffset + payRateOffset - 22

        output = "{0}{1:>%d}{2:>%d}{3:>%d}" % (shiftOffset, payRateOffset, hourOffset)
        output = output.format(nameCombo,
                emp.getShiftNumber(),
                emp.getPayRate(),
                emp.getHoursWorked())

        # Print the formatted string
        print(output)

    # Used to print all employees
    def printPWs(self):
        
        # Print the header
        print("ID | Name          |Shift|     |Pay-Rate|     |Hours Worked|")
        print("------------------------------------------------------------")
        
        # Loop through and print all employees
        for key in self.productionWorkers:
            self._printPW(self.productionWorkers[key])
    
    # End ShiftManager class

# Make sure this script is only used as a module
if (__name__ == "__main__"):
    print("This script is only to be used as a module!")
    quit()
