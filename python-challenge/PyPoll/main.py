import pandas as pd
import os

# Load the dataset
file_path = 'python-challenge/PyPoll/resources.pypoll/election_data.csv'
data = pd.read_csv(file_path)

# Calculate the total number of votes
total_votes = len(data['Voter ID'])

# Get a complete list of candidates who received votes
candidates = data['Candidate'].unique()

# Calculate the vote counts and percentages for each candidate
vote_counts = data['Candidate'].value_counts()
vote_percentages = (vote_counts / total_votes) * 100

# Determine the winner based on popular vote
winner = vote_counts.idxmax()

# Print the results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for candidate in candidates:
    print(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})")
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")

# Ensure the output directory exists
output_dir = 'pypoll_analysis'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_path = os.path.join(output_dir, 'election_results.txt')

# Export the results to a text file
with open(output_path, 'w') as file:
    file.write("Election Results\n")
    file.write("-------------------------\n")
    file.write(f"Total Votes: {total_votes}\n")
    file.write("-------------------------\n")
    for candidate in candidates:
        file.write(f"{candidate}: {vote_percentages[candidate]:.3f}% ({vote_counts[candidate]})\n")
    file.write("-------------------------\n")
    file.write(f"Winner: {winner}\n")
    file.write("-------------------------\n")