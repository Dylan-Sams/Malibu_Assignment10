# API.py
# Student Name: Dylan Sams, Alisha Siddiqui, Colton Ramsey, Leah Radcliffe
# email:  samsds@mail.uc.edu, ramseyc6@mail.uc.edu, radclilr@mail.uc.edu, siddiqas@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: In this assignment we will execute an API to get results from, then we will extract some interesting data to print to the console and write to a CSV file.

# Brief Description of what this module does. This module instantiates the class API_Load which runs a data request to the Incoome Tax API.
# Citations: API: https://api-ninjas.com/api/incometax

# Anything else that's relevant


import json
import requests

class API_load:
    """
    Runs the URL API request and parses the returned data into a python data structure.
    """
    def __init__(self):
        """
        Constructor
        """

    def load_API(self):
        """
        Loads the 2025 national income tax brackets from an API URL.
        @return parsed_json dict: python dictionary of the data returned from the API.
        """
        response = requests.get('https://api.api-ninjas.com/v1/incometax?country=US&year=2025', headers={'X-Api-Key': 'TQpOkYeBiyYoHVbkxVmS+A==qHUiL3KyQifZujA4'})
        json_string = response.content

        parsed_json = json.loads(json_string)
        return parsed_json