# Add dependencies
import csv
import os

# Asssign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.text")

# 1. Initialize a total vote counter.
total_votes = 0

# Create a list of Candidates
candidate_options = []
# Declare an empty dictionary for candidates' votes
candidate_votes = {}
# Declare a variable that holds an empty string value for the winning candidate
winning_candidate = ""
# Declare a variable for the "winning count" equal to zero
winning_count = 0
# declare a variable for the winning percentage equal to zero
winning_percentage = 0



# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    #Print each row in the csv file.
    for row in file_reader:

        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # initiate for loop to only add names once
        if candidate_name not in candidate_options:

            # Add candidate name to candidate options
            candidate_options.append(candidate_name)
        
            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count
        candidate_votes[candidate_name] +=1

    # Save the the results to out text file.
    with open(file_to_save, "w") as txt_file:
        
        # Print the final vote count to the terminal.
        election_results  =(
        f'\nElection Results\n' 
        f'----------------------\n'
        f'Total Votes: {total_votes:,}\n'
        f'----------------------\n')
        print(election_results, end='')
        # save the final vote count to the text file.
        txt_file.write(election_results)

        # Determine the percentage of votes for each candidate by looping through the counts.
        # Iterate through the candidate list.
        
        for candidate_name in candidate_options:
            # retrieve vote count of a candidate.
            votes = candidate_votes[candidate_name]
            # calculate the percentage of votes.
            vote_percentage = float(votes)/float(total_votes)*100
            
            # print each candidate, their vote count, and percentage to the terminal.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)

            # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                # If true then set winning_count = votes and winning_percent = vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage
                    
                # set the winning_candidate equal to the candidate's name.
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")

        print(winning_candidate_summary)
        # save the winning candidate's same to the text file.
        txt_file.write(winning_candidate_summary)

