import csv
import os
file_to_load = os.path.join("Resources", "election_data.csv")
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
#first we start with open file
with open(file_to_load) as polling_data:
    #reader is a function of the csv module imported on line 1
    reader = csv.reader(polling_data)
    #skip the header but save as a variable header
    header = next(reader)
# The total number of votes cast
#count each row to sum total votes
    total_votes =0
    candidates= [] #general candidates list
    
   



    for vote in reader:
        total_votes += 1  #+= total_votes = total_votes +1
        #who is actually a candidate
        #iterate through reader to identify candidates
        
        #add the unique candidates to that list 
        #append method to add unique candidates to that list
        #check to see if this list has a candidate before add
        #if khan is in the list then add it to the unique candidate list
        #create a dict to hold the unique candidate names 
        #create a list for candidates
        candidates= (["Khan", "O'Tooley", "Correy", "Li"])
    print(candidates[1])
    print(candidates[1])
    print (candidates[2])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
    print(candidates[3])  
     
    

        

print(f"Total Votes: {total_votes}\n")
#print=(f"Candidates: {candidates}\n")


#   * A complete list of candidates who received votes

#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

 


