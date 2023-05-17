#Import modules
import os
import csv

#Total number of votes cast <<<
#Complete list of candidates who received votes <<<
#Percentage of votes each candidate won
#Total number of votes each candidate won
#Winner of the election

#ballot id [0]
#county [1]
#candidate [2]

total_votes = 0
vote_percents = 0
candidate_vote_total = 0

ballot_id = []
candidates = []
candidate_vote_percent = []
votes_per_candidate = []

#Path and reader, without header
votes_csv = os.path.join("Resources", "election_data.csv")
with open(votes_csv) as vote_file:
    vote_reader = csv.reader(vote_file)
    header = next(vote_reader)
    
    #total votes
    total_votes = len(list(vote_file))
    
    #Candidate list
    for row in vote_reader:
        candidates.append(row[2])
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate) 
            
    #Perentage of votes each candidate won
    for row in vote_reader:
        candidates.append[2]
        candidate = row[2]

        if candidate == candidates:
            candidate_vote_total += 1
        
    
        

        #ballot_id.append(row[0])
        #candidate.append(row[2])
        
        #ballot_id = (row[0])
        #county = (row[1])
        #candidate = (row[2])
        #store "location" of empty list here ?
        #candidate_vote_total.append(vote_reader)

        #total_votes = len(list(ballot_id))
        #print(total_votes)

        #print("Candidates are:" + ", ".join(candidate for candidate in candidates))

    #List Candidates
        #i = 0
    # for i in row:

        # candidates.append(str(candidate[i]))

        # if str(candidate[i]) != str(candidate[i - 1]):
        #     candidates.append(str(candidate[i]))

            

        #     #candidate_vote_total.append(int(candidate_total)) #???
        
        #     candidate_name = str(candidate[i])
        #     print(f"{candidate_name}")
        #     candidate_total = 0

        # elif str(candidate[i]) == str(candidate[i - 1]):
        #     candidate_total += 1


    #Percent of votes and total votes for each candidate
    #o = 0
    #for o in vote_reader:

        
        
#print(f"Total Votes: {total_votes}")
print(candidates)
        

