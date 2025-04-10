# JSON_to_CSV.py
# Student Name: Dylan Sams, Alisha Siddiqui, Colton Ramsey, Leah Radcliffe
# email:  samsds@mail.uc.edu, ramseyc6@mail.uc.edu, radclilr@mail.uc.edu, siddiqas@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: In this assignment we will execute an API to get results from, then we will extract some interesting data to print to the console and write to a CSV file.

# Brief Description of what this module does. {Do not copy/paste from a previous assignment. Put some thought into this. required}
# Citations: {"Stack Overflow" is not sufficient. Provide repeatable links, book page #, etc.}

# Anything else that's relevant


# to-do for this module
# Write the JSON dictionary saved from the API_load class in API.py to a CSV file and save in the data folder


import csv

class JSON_to_CSV:
    def __init__(self, json_data, file="output.csv"):
        self.data = json_data
        
    def write_to_csv(self):
        with open(self.file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(self.data[0].keys() if isinstance(self.data, list) else self.data.keys())
            writer.writerows(item.values() for item in self.data) if isinstance(self.data, list) else writer.writerow(self.data.values())
