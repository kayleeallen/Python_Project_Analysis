# The data we need to retrieve
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

import csv
import os

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis", "Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis","analysis", "election_analysis.txt")

# Open the Selection results and read the file.
with open(file_to_load) as election_data:


     #To do: read and analyze the data here.
     # Read the file object with the reader function
     file_reader = csv.reader(election_data)
     #Print header row
     headers = next(file_reader)
     print(headers)
     



