# main.py
# Student Name: Dylan Sams, Alisha Siddiqui, Colton Ramsey, Leah Radcliffe
# email:  samsds@mail.uc.edu, ramseyc6@mail.uc.edu, radclilr@mail.uc.edu, siddiqas@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: In this assignment we will execute an API to get results from, then we will extract some interesting data to print to the console and write to a CSV file.

# Brief Description of what this module does. This module creates an instance of the classes API_Load(), dataProcessing(), and JSON_to_CSV. Then, runs the modules in the classes
# Citations: 

# Anything else that's relevant

from dataProcessingPackage.dataProcessing import *
from dataProcessingPackage.JSON_to_CSV import *
from APIPackage.API_load import *
import json
import requests

if __name__ == "__main__":
    API = API_load()
    json_data = API.load_API()

    dataProcess = dataProcessing(json_data)
    marriage_tax_brackets = dataProcess.extract_bracket_data()
    
    json_conversion = JSON_to_CSV(json_data)
    CSV = json_conversion.write_to_csv()
    