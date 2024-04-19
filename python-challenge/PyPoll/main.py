import csv

# Read the election data from the CSV file
with open('election_data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header row
    total_votes = 0
    candidate_votes = {}

    for row in reader:
        total_votes += 1
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

# Calculate the percentage of votes each candidate won
candidates = list(candidate_votes.keys())
winner = candidates[0]
max_votes = candidate_votes[winner]
total_percentage = 0

print("Election Results")
print("-------------------------")
