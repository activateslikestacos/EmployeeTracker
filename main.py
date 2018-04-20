# File Name: main.py
# Developer: Christopher Cox
# Date last modified: 11/25/2017
# Description: The main driver file for the Employee tracker program.
#     This program reads employee data from a file called employees.csv
#     and outputs it to the screen in a formatted manner
#
# E-Mail: thetaco.dyndns@gmail.com

# Import our production worker class
from ProductionWorker import ProductionWorker
from ShiftManager import ShiftManager
import csv
import os

FILE_NAME = 'employees.csv'

# Generates a ProductionWorker object with the supplied CSV line
def generatePW(csv):

    # Format is as follows:
    # name = 1, ID = 0, shift = 2, payRate = 3, initHours = 4
    return ProductionWorker(csv[1], csv[0], csv[2], csv[3], csv[4])

def start():

    # Make sure the file exists
    if(not os.path.exists(FILE_NAME)):
        print(FILE_NAME, "doesn't exist! Aborting")
        quit()

    # Create shiftManager object
    sManager = ShiftManager()

    # Use the with statement to create a context manager
    with open(FILE_NAME, 'r') as eFile:

        # Use the csv module to easily parse the file
        employee_data = csv.reader(eFile, delimiter=',')

        # Populate employee list
        for item in employee_data:
            sManager.addPW(generatePW(item))

    # List all production workers using shift manager
    sManager.printPWs()


# Make sure this is not being imported as a module
if (__name__ == "__main__"):
    start()
