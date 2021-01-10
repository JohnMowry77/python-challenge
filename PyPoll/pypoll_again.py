import csv
import os
file_to_load = os.path.join("Resources", "election_data.csv")
#output_path = os.path.join("")
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
#first we start with open file
with open(file_to_load) as polling_data:
    #reader is a function of the csv module imported on line 1
    reader = csv.reader(polling_data)
    #skip the header but save as a variable header
    header = next(reader)
    #candidates_list =[]
#print(header)
    for row in reader:
        print(",", end=""),    
        total_votes = total_votes + 1 #Add to the total vote count
        #print(total_votes)
        candidate_name = row[2] #Extract the candidate name from each row
        #the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #Add it to the list of candidates in the running
            candidate_options.append(candidate_name)

            #And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        #Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1
print(candidate_votes)

  #*The total number of votes cast

  #*A complete list of candidates who received votes

  #*The percentage of votes each candidate won

  #*The total number of votes each candidate won

 #*The winner of the election based on popular vote.