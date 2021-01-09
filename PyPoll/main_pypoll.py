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
    #Find the total number of votes cast
    
    total_votes =0
     #create a list for candidates
    candidates= [] #general candidates list
    #unique_names= {"Khan": "votes fore ach start 0"} #create a dict where Unique_Candidates are keys
    #and the vote for each starts at 0
    #then create a loop to calculate the total votes
    
    # * A complete list of candidates who received votes

    for vote in reader:
        total_votes += 1  #+= total_votes = total_votes +1
        #iterate through reader to identify candidates
        candidates_name= vote[2]
        #unique_candidates=vote[2]
        #count each number of candidates in the list
        #add the unique candidates to that list
        #unqiue_name= (["Khan", "O'Tooley", "Correy", "Li"])
        #if candidates_name is in the list then add it to the unique candidate list
        if candidates_name not in candidates: #if candidates_name is not currently in the candidates list append it
            #candidates.append("some candidate")
            candidates.append(candidates_name)
            #add the unique candidates to that list
            #khan=int(candidates.count("Khan"))
    #print(candidates_name)

       #khan=int(candidates.count("Khan")) #Count each number in the candidates list        
            

        #if candidates_name not in unique_candidates:
            #candidates.append(uniuqe_candidates)

            #print()
            
print(f"Vote Analysis\n")
print(f"----------------------------\n")  #print space in between 
print(f"Total Votes: {total_votes}\n")
print=(f"Candidates: {candidates}\n")




#   * The percentage of votes each candidate won

#   * The total number of votes each candidate won

#   * The winner of the election based on popular vote.

 
# We can also add conditional logic (if statements) to a list comprehension
#july_temperatures = [87, 85, 92, 79, 106]
# hot_days = []
# for temperature in july_temperatures:
#     if temperature > 90:
#         hot_days.append(temperature)
# print(hot_days)


# # List comprehensions provide concise syntax for creating lists
# letters=[len(each_item) for each_item in fish] # add each item to a new list
# letters = [letter for letter in fish]
# print(letters)