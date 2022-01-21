# Election Analysis
## Project Overview
The purpose of this election audit is to independently determine the the winner of the recent local congressional election and send the results to the Colorado board of Elections. 
## Election Audit Results:

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

* To determine the number of votes for each county and the percentage of the total votes that each one held, the following code was implemented. 

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

* The following code determines the county with the most votes. It tracks the votes for eaach county and then shares the results of the county with the most votes to the text file.

------------

**largest_county = ""** ( creates a string to hold the county's name with the most votes)

**largest_county_votes = 0** (creates a varaible defined as a variable with a value of zero to hold the place of the votes for the number of votes)

**largest_county_percentage = 0** (same purpose as the line above but intended for a percentage of total votes)

**for county_name in county_options:** (initiates a for loop that gets the county's name from the county dictionary)

**votes_co = county_votes.get(county_name)** (creates a variable to hold the county's votes for the specified county)

**county_vote_percentage = float(votes_co)/float(total_votes)100** (calculates the percentage of total votes)

**county_results = (f'{county_name} county: {county_vote_percentage:.1f}% ({votes_co:,})\n')** (defines the county's results including it's name, percentage, and vote count)

**if (votes_co > largest_county_votes) and (county_vote_percentage > largest_county_percentage):** (Initiates an if statement that determines the county with the largest vote count and what that count is)

**txt_file.write(county_results)** (writes the results to the text file concerning the county specific results)

------------

* The next section collects the results for each candidate and writes them in a summary to the text file.

------------

    for candidate_name in candidate_votes:

        # Retrieve vote count and percentage
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
        candidate_results = (
            f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n\n")

------------

* Lastly, the following code determines the winner of the election, their vote count and what percentage of the total votes they received:

------------

        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

------------

## Eleciton Audit Summary

This script of code has been constructed to read and print data from the CSV file as if it were any CSV file with any data with three columns. There are references in the code to each row and column pair, signifying that there is an assumption that every data point in a given column type and that each row of data is associated with a single voter. This code isn't specific to the colorado congressional election vote and can be used for any election as long as the data is formatted as just described. However, slight modifications requiring little adjustment of the script can allow for more inputs. For example, if each vote had the voters' age in the fourth column of the csv file data, then the code can stay exaclty as it is with only the addeitional code to analyzed and compare votes for different candidate in a given age range or give an aerage voter age for each county. The other convenient thing about this code is that no additional editing is required if there are more counties involved, more candidates to vote for, or more voters turning in ballots. It would simply increase the lists and dictionaries that would eventually be printed in the tewxt file for the summary as normal. 
