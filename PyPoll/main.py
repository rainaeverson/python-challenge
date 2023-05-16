#Import modules
import os
import csv

#Total number of votes cast
#Complete list of candidates who received votes
#Percentage of votes each candidate won
#Total number of votes each candidate won
#Winner of the election

#ballot id [0]
#county [1]
#candidate [2]

total_votes = 0
vote_percents = 0
candidate_total = 0

ballot_id = []
county = []
candidate = []
candidates = []
candidate_vote_percent = []
candidate_vote_total = []

votes_csv = os.path.join("..", "Resources", "election_data.csv")

with open(votes_csv) as vote_file:
    vote_reader = csv.reader(votes_csv)
    header = next(vote_reader)

    #total_votes = len(list(vote_file))
    #print(total_votes)

    for row in vote_file:
        ballot_id.append(vote_file[0])
        county.append(vote_file[1])
        candidate.append(vote_file[2])

        total_votes = len(ballot_id)
    print(total_votes)
