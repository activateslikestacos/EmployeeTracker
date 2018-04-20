# File Name: ProductionWorker.py
# Developer: Christopher Cox
# Date last modified: 12/11/2017
# Description: Another simple file holding a class named ProductionWorker.
#     ProductionWorker is a subclass of Employee, thus adding a few more
#     functions and data members.
#
# E-Mail: thetaco.dyndns@gmail.com

# Import over only the Employee class
from Employee import Employee

# Create new class, setting Employee as subclass
class ProductionWorker(Employee):
    
    # Helpful variables to set shift to either day or night
    DAY = 1
    NIGHT = 2

    # 'Private' data members
    _shiftNumber = None
    _payRate = None
    _hoursWorked = None

    # Constructor
    def __init__(self, name, ID, shift, payRate, initHours):

        # Call constructor of base class
        Employee.__init__(self, name, ID)

        # Initialize class variables
        self._shiftNumber = shift
        self._payRate = payRate
        self._hoursWorked = initHours

    # Accessor and modifier methods
    def getShiftNumber(self):
        return self._shiftNumber

    def setShiftNumber(self, shift):
        self._shiftNumber = int(shift)

    def getPayRate(self):
        return self._payRate

    def setPayRate(self, rate):
        self._payRate = float(rate)

    def getHoursWorked(self):
        return self._hoursWorked

    def addHoursWorked(self, amount):
        self._hoursWorked = self._hoursWorked + float(amount)

    def setHoursWorked(self, amount):
        self._hoursWorked = float(amount)

    # End ProductionWorker class

# Once again making sure this is only being used as a module
if (__name__ == "__main__"):
    print("This script is only to be used as a module!")
    quit()
