#!/usr/bin/env python
# coding: utf-8

# # PyPoll

# In[10]:


import os
import csv

csv_path = os.path.join(".","Resources","election_data.csv")
output_file = os.path.join(".","election_analysis.txt")

total_votes = 0

candidate_votes = {}
candidate_options = []

candidate_winner = "" 
count_of_wins = 0


with open(csv_path) as election_data:
    read = csv.reader(election_data)
    
    header = next(read)    
    #print(header)
    
    for row in read:
        total_votes = total_votes + 1
        #print(row)
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            #print(candidate_name)
            candidate_votes[candidate_name] = 0
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

#print(candidate_votes)
#print(candidate_options)            


with open(output_file, "w") as txt_file: 
    election_results = (
    f"Election Results\n"
    f"----------------------------\n"
    f"Total Votes {total_votes}\n"
    f"----------------------------\n"
    f"{candidate_name}:\n"
    
        
    )
    print(election_results)
    
    txt_file.write(election_results)
    
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        votes_percent = float(votes) / float(total_votes) *100
         
    if (votes > count_of_wins):
        count_of_wins = votes
        candidate_winner = candidate
        
        voter_output = f"{candidate} : {votes_percent:.3f}% ({votes})\n)"
        #print(votes)
        #print(votes_percent)
        print(voter_output)
        txt_file.write(voter_output)
        
    winner_output = (
    f"------------------------------\n"
    f"Winner: {candidate_winner}\n"
    f"---------------------------\n"
    )
print(winner_output)

#Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


# In[ ]:





# In[ ]:




