import csv
import os
file_to_load = os.path.join("Resources", "election_data.csv")
#output_path = os.path.join("")
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
#first we start with open file
with open(file_to_load) as polling_data:
    #reader is a function of the csv module imported on line 1
    csvreader = csv.reader(polling_data)
    #skip the header but save as a variable header
    header = next(csvreader)
    
pypoll = {} #call the dict pypoll
candidates= {"candidate1": "Khan", "candidate2": "Correy", "candidate3": "Li", "candidate3": "OTooley"}
    #print(candidates)
poll_win= 0
for x, y in candidates.items():
    if y > poll_win:
        poll_win_count = y
        poll_win_name = x
print (f"{poll_win_name}-{poll_win_count}")