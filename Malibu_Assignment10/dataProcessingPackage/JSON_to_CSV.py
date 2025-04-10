# JSON_to_CSV.py
# Student Name: Dylan Sams, Alisha Siddiqui, Colton Ramsey, Leah Radcliffe
# email:  samsds@mail.uc.edu, ramseyc6@mail.uc.edu, radclilr@mail.uc.edu, siddiqas@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: In this assignment we will execute an API to get results from, then we will extract some interesting data to print to the console and write to a CSV file.

# Brief Description of what this module does. This module instantiates the class JSON_to_CSV which turns the json file from the API into a CSV file.
# Citations: CSV: https://docs.python.org/3/library/csv.html
# Save csv file to specific folder: https://stackoverflow.com/questions/52842831/how-to-save-csv-file-to-specific-folder/52842932

# Anything else that's relevant

import csv
import os

class JSON_to_CSV:
    """
    Converts JSON data returned by the API into a CSV file.
    """
    def __init__(self, json_data, file="output.csv"):
        """
        Constructor
        @parameters json_data dict: The data to be processed.
        @parameters file str: The CSV file to be written to.
        """
        self.data = json_data
        self.file = os.path.join("Data", file)
    def write_to_csv(self):
        """
        Converts the json python dictionary to a CSV file.
        """
        with open(self.file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.data[0].keys() if isinstance(self.data, list) else self.data.keys())
            writer.writerows(item.values() for item in self.data) if isinstance(self.data, list) else writer.writerow(self.data.values())
