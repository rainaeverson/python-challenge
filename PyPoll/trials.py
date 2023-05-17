with open(votes_csv) as vote_file:
    vote_reader = csv.reader(vote_file)
    header = next(vote_reader)
    

    total_votes = len(list(vote_file))
    
    #Candidate list
    for row in vote_reader:
        candidates.append(row[2])
        candidate = row[2]
        
        if candidate not in candidates:
            candidates.append(candidate) 
        

    for row in vote_reader:
        candidates.append[2]
        candidate = row[2]

        if candidate == candidates:
            candidate_total += 1