# First, import the os module
# This will allow us to create file paths across operating systems
import os

#Module for reading CSV files
import csv

#call out path to initial data file
csv_path = os.path.join('Resources', 'election_data.csv')

#Create variable for the output text file
output_file = 'election_output_results.txt'

#Specify the file path for saving the output text file
output_file_path = os.path.join('Analysis', output_file)

# Analyze election data
def analyze_election_data(csv_path):
    # total number of votes cast
    # A complete list of candidates who received votes
    # the percentage of votes each candidate won
    # total number of votes each candidate won
    # the winner based on popular vote

    # Read through csv file, skipping the header row
    with open(csv_path, 'r') as csvfile:
        # Read the initial CSV file
        csvreader = csv.reader(csvfile, delimiter= ',')
        next(csvreader)

        # list
        candidate_names = []
        # dictionary
        candidate_votes = {}
        total_votes = 0
        max_votes = 0
        winner = ""
        voter_output = ""

        for iteration in csvreader:
            total_votes += 1
            candidate = iteration[2]
            
            if candidate not in candidate_votes:
                # creates key of the candidate if not already in candidate_votes dictionary, and assigns it a value of 0
                candidate_votes[candidate] = 0

                # key = candidate_votes[candidate]
                # value = 0
                # {"Charles": 0, "Diana": 0,"Last candidate": 0}
            
            # Below line is occuring outside the above "if" statement for each iteration in csvreader
            candidate_votes[candidate] += 1
        
            if candidate not in candidate_names:
                 # appending candidate name if not in candidate names list
                candidate_names.append(candidate)

        for candidate, votes in candidate_votes.items():
            percentage = (votes / total_votes) * 100 if total_votes > 0 else 0
            voter_output += f"{candidate}: {percentage:.3f}% ({votes})\n"
            
            if votes > max_votes:
                max_votes = votes
                winner = candidate


        print(winner + ": " + str(max_votes))

        with open(output_file_path, 'w') as output_file:
        # Print the final vote count
            output_file.write("Election Results\n")
            output_file.write("-------------------------\n")
            output_file.write(f"Total Votes: {total_votes}\n")
            output_file.write("-------------------------\n")
            output_file.write(f"{voter_output}")
            output_file.write("-------------------------\n")
            output_file.write(f"Winner: {winner}\n")
            output_file.write("-------------------------\n")

        # Print the results to the console
        print("Election Results")
        print("-------------------------")
        print(f"Total Votes: {total_votes}")
        print("-------------------------")
        print(f"{voter_output}")
        print("-------------------------")
        print(f"Winner: {winner}")
        print("-------------------------")

# Call the function with the specified CSV file path
analyze_election_data(csv_path)
