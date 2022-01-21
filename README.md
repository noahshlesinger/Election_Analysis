# Election_Analysis
## Project Overview
The purpose of this election audit is to independently determine the the winner of the recent local congressional electoin and send the results to the Colorado board of Elections. 
## Election_Audit Results:

The following points are main metrics and outcomes of the audit:

* **The total number of votes in the congressional election was 369,711 votes** across the three counties. This code imports the csv module needed in order to read the file containing the election data, creates a path between the csv file and the python file that is running the analysis, initializes a variable to hold the votes, then runs a for loop through the data to count all of the votes.
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

* To determine the number of votes for each county and the percentage of the total votes that each one held, the following code was implemented: 

-------------

**county_options = []** (creates an empty list to be filled with all counties)

**county_votes = {}** (Creates a dictionary to hold attach each county and it's votes)

**county_name = row[1]** (defines a variable to name the county by pulling from the second column in the csv data)

**if county_name not in county_options:**(initiates an if statement to only add a county's name to the list of options once)

**county_options.append(county_name)** (adds the county's name to the list if not already listed)

**county_votes[county_name] = 0** (Now that it has been added to the list, it is given a vote count of 0 to start)

**county_votes[county_name] += 1** (this line is outside the if statement and adds a 1 to the current count of the county's vote)

**with open(file_to_save, "w") as txt_file** (allows opens a text file to write and record these results)

**txt_file.write(county_results)** (writes the results to the text file concerning the county specific results)

-------------

* The following code determines the county with the most votes.

------------

**largest_county = ""** ( creates a string to hold the county's name with the most votes)

**largest_county_votes = 0** (creates a varaible defined as a variable with a value of zero to hold the place of the votes for the number of votes)

**largest_county_percentage = 0** (same purpose as the line above but intended for a percentage of total votes)

**for county_name in county_options:** (initiates a for loop that gets the county's name from the county dictionary)

**votes_co = county_votes.get(county_name)** (creates a variable to hold the county's votes for the specified county)

**county_vote_percentage = float(votes_co)/float(total_votes)100** (calculates the percentage of total votes)

**county_results = (f'{county_name} county: {county_vote_percentage:.1f}% ({votes_co:,})\n')** (defines the county's results including it's name, percentage, and vote count)



------------


* Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.

* Which candidate won the election, what was their vote count, and what was their percentage of the total votes?




















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
