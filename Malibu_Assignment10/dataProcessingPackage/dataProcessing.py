# dataProcessing.py
# Student Name: Dylan Sams, Alisha Siddiqui, Colton Ramsey, Leah Radcliffe
# email:  samsds@mail.uc.edu, ramseyc6@mail.uc.edu, radclilr@mail.uc.edu, siddiqas@mail.uc.edu
# Assignment Number: Assignment 10
# Due Date:   4/10/2025
# Course #/Section:  IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment: In this assignment we will execute an API to get results from, then we will extract some interesting data to print to the console and write to a CSV file.

# Brief Description of what this module does. This module instantiates the class dataProcessing which extracts the tax brackets for married couples into a readable format.
# Citations: Dictionaries: https://www.w3schools.com/python/python_dictionaries_access.asp
# getting specifics from dictionary: https://note.nkmk.me/en/python-dict-get/

# Anything else that's relevant

class dataProcessing:
    """
    Processes JSON data returned from the API and prepares it for use or CSV export.
    """

    def __init__(self, json_data):
        """
        Constructor
        @parameters json_data dict: The data to be processed.
        """
        self.data = json_data

    def extract_bracket_data(self):
        """
        Extracts income tax brackets from the JSON into a list of dictionaries.

        @return list[dict]: Each dict contains 'income' and 'rate' keys.
        """
        bracket_data = []

        brackets = self.data["federal"]["married"]["brackets"]
        print("Federal tax brackets for married couples in the US:")
        increment = 1
        for bracket in brackets:
            min = bracket.get("min", "N/A")
            max = bracket.get("max", "N/A")
            rate = bracket.get("rate", "N/A")

            print(f"{increment}: Minimum Income: {min}, Maximum Income: {max}, Tax Rate: {rate}")
            increment += 1

            bracket_data.append({
                "min": min,
                "max": max,
                "rate": rate
            })
            

        return bracket_data
