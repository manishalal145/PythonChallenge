# Importing dependencies
import os
import csv

# Set path for file
data_csv = os.path.join("PyPoll", "Resources", "election_data.csv")

# Declarations
candidate_dict = {}
percent_votes = []

# Total Vote Counter
total_votes = 0

# Open and read csv
with open(data_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    for row in csv_reader:

        # Total votes in the election
        total_votes += 1

        # Extract the candidate name from each row
        candidate = row[2]

        # If the candidate is the dictionary key
        if candidate in candidate_dict.keys():
            candidate_dict[candidate]+=1
        else:
            candidate_dict[candidate]=0

# Winner
    for key in candidate_dict.keys():
        if candidate_dict[key] == max(candidate_dict.values()):
            winner_candidate = key

# To terminal:
print(f"Election Results\n")
print("-------------------------\n")
print(f"Total Votes: {total_votes}\n")
print("-------------------------\n")
# Percentage calculation
for i in candidate_dict:
    percent_votes = round(float(candidate_dict[i])/total_votes * 100, 2)
    print(f"{i} : {percent_votes}% ({candidate_dict[i]})\n")
print("-------------------------\n")
print(f"Winner: {winner_candidate}\n")
print("-------------------------\n")


# Create analysis file
election_file = os.path.join("PyPoll", "Analysis", "election_data.txt")
with open (election_file, 'w') as outputfile:
    outputfile.write(f"Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total Votes: {total_votes}\n")
    outputfile.write("-------------------------\n")
    # Percentage calculation
    for i in candidate_dict:
        percent_votes = round(float(candidate_dict[i])/total_votes * 100, 2)
        outputfile.write(f"{i} : {percent_votes}% ({candidate_dict[i]})\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Winner: {winner_candidate}\n")
    outputfile.write("-------------------------\n")
