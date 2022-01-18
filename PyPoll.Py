# Add dependencies
import csv
from importlib.resources import path
import os

# Asssign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.text")

# Open the election results and read the file.
with open(file_to_load) as election_data:
   
    # To do: read and analyze the data here.
    file_reader = csv.reader(election_data)

    # Read and Print the header row.
    headers = next(file_reader)
    print(headers)  