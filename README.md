# Election_Analysis
## Project Overview
The purpose of this election audit is to independently determine the the winner of the recent local congressional electoin and send the results to the Colorado board of Elections. 
## Election_Audit Results:
Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.
The following points are main metrics and outcomes of the audit:

How many votes were cast in this congressional election?
* The total number of votes in the congressional election was 369,711 votes across the three counties. To determine this, the following code was applied:
-------------
**import csv** (imports csv module to deal with CSV files)

**import os**

**file_to_load = os.path.join( "Resources", "election_results.csv")** (joins the csv file with the python file to allow the csv data to be used)

**file_to_save = os.path.join("analysis", "election_analysis.txt")** (creates a path between the python file to the output text file where the results will be displayed)

**total_votes = 0** (initializes a variable to count the total votes)

**with open(file_to_load) as election_data:** (opens the csv file)

**reader = csv.reader(election_data)** (reads the csv file)

**header = next(reader)** (distinguishes that the first row is only headers and not data itself)

 **for row in reader:** (creates a for loop to loop through all the rows in the csv file)
 
 **total_votes = total_votes + 1** (adds 1 to the total vote count every time it sees a vote)

-------------

This code imports the csv module needed in order to read the file containing the election data, creates a path between the csv file and the python file that is running the analysis, initializes a variable to hold the votes, then runs a for loop through the data to count all of the votes.

Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.

Which county had the largest number of votes?

Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

Which candidate won the election, what was their vote count, and what was their percentage of the total votes?




















A Colorado Board of Elections employees has given you the following tasks to complete the eleciton audit of a recent local congressional election.
1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes.
3. Calculate teh total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.

## Resources
* Data Source: election_results.csv
* Software: Python 3.10.1, Visual Studio Code, 1.38.1

## Summary
The analysis of the election show that:
* There were "x" votes cast in the election.
* The candidates were:
  * Candidate 1
  * Candidate 2
  * Candidate 3
* The candidate results were:
  * Candidate 1 received"x%" of the vote and "Y" number of votes.
  * Candidate 2 received"x%" of the vote and "Y" number of votes.
  * Candidate 3 received"x%" of the vote and "Y" number of votes.
* The winner of the election was:
  * Winning Candidate, who received "x%" of the vote and "y" number of votes.

## Challenge Overview
The election comission has requested some additional data to complete the audit.
1. The voter turnout for each county
2. The percentage of votes from each county out of the total count
3. The county with the highest turnout.
4. Print All Election Results to the Command Line and Saved to a Text File
## Challenge Summary
