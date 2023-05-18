#Import modules
import os
import csv

#Total number of votes cast <<<
#Complete list of candidates who received votes <<<
#Percentage of votes each candidate won
#Total number of votes each candidate won
#Winner of the election

total_votes = 0
vote_percents = 0
candidate_vote_total = 0
winning_candidate = ""
winning_vote_total = 0
percentage_votes = 0

ballot_id = []
candidates = []
candidate_votes = {}
candidate_total = []

#Path and reader, without header
votes_csv = os.path.join("Resources", "election_data.csv")
with open(votes_csv) as vote_file:
    vote_reader = csv.reader(vote_file)
    header = next(vote_reader)
    
    #Candidate list & total votes
    for row in vote_reader:
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            candidate_votes[row[2]] = 0
        candidate_votes[row[2]] += 1
    print("")
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("")

    #Percentage of votes & adding total, percents to candidate dictionary
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        percentage_votes = round(float(votes) / float(total_votes) * 100, 3)
        candidate_votes[row[2]] += percentage_votes

        if votes > winning_vote_total:
            winning_vote_total = votes
            winning_candidate = candidate
    
    print(f"Charles Casper Stockham: {percentage_votes}% {candidate_votes['Charles Casper Stockham']}")
    print(f"Diana DeGette: {percentage_votes}% {candidate_votes['Diana DeGette']}")
    print(f"Raymon Anthony Doane: {percentage_votes}% {candidate_votes['Raymon Anthony Doane']}")
    print("")
    print("--------------------------")
    print("")
    print(f"Winner: {winning_candidate}")
    print("")
    print("---------------------------")

    #Export to text file
f = open("analysis.txt", "w")

print ("", file=f)
print ("Election Results", file=f)
print ("-------------------------", file=f)
print (f"Total Votes: {total_votes}", file=f)
print ("", file=f)
print (f"Charles Casper Stockham: {percentage_votes}% {candidate_votes['Charles Casper Stockham']}", file=f)
print (f"Diana DeGette: {percentage_votes}% {candidate_votes['Diana DeGette']}", file=f)
print (f"Raymon Anthony Doane: {percentage_votes}% {candidate_votes['Raymon Anthony Doane']}", file=f)
print ("", file=f)
print ("--------------------------", file=f)
print ("", file=f)
print (f"Winner: {winning_candidate}", file=f)
print ("", file=f)
print ("---------------------------", file=f)

f.close()

        

