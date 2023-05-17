#Import modules
import os
import csv

candidates = []
candidate_total_list = []
candidate_name_list = []
candidate_vote_total = 0

votes_csv = os.path.join("Resources", "election_data.csv")
with open(votes_csv) as vote_file:
    vote_reader = csv.reader(vote_file)
    header = next(vote_reader)
    
    for row in vote_reader:
        if row[2] not in candidates:
            candidates.append(row[2])
            
        #     candidate_total_list.append(row[2])
        #     candidate_total = 0
        # else:
        #     candidate_total += 1

        #elif row[2] == candidates:
            #candidate_total += 1
    
    #Total votes per candidate
    for votes in vote_reader:
        if votes[2] == candidates[votes - 1]:
            candidate_vote_total += 1
            
        else:
            candidate_name_list.append(str(votes[2]))
            candidate_total_list.append(int(candidate_vote_total))
            candidate_vote_total = 0
            

print(f"The candidates are: {candidates}")
print(f"{candidate_name_list} + {candidate_total_list}")
