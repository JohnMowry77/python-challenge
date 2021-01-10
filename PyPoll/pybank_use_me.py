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
    #Candidates List Holders
    candidates_dup = []
    candidate_list =[]
    total_votes = 0

    #for each row
    for row in csvreader:
        #run the loader animation
        #print(", ", end="")
        #add to the toal vote count
        #total_votes = total_votes +1
        candidates_dup.append(row[2]) #add candidates name to candidates_dup list candidates start in row 2
        candidate_list = set(candidates_dup) #use set property to remove duplicate from candidate dup list
        candidate_list = list(candidate_list) #convert to list
        number_candidates= len(candidate_list) #how many candidates
        #print(number_candidates) #Print number_candidates  result is 4
        total_votes= len(candidates_dup)
        #print(total_votes)    

        #extract the candidate naem from each row
        #candidate_name= row[2] #you skipped the header already
        #candidates_votes= []
        #pypoll = {} #call the dict pypoll (unorderd,changeable and does not allow duplicates)
        #dict_keys= (['OTooley', 'Correy', 'Khan', 'Li'])
        #dict_values= ([105630, 704200, 2218231, 491940])

        #if the candidate does not match any existing candidate add candidate 
        #(loop is "disvoering" candidates as it goes)
        #if candidate_name not in candidate_list:
            # add it to the list of candidates in the running
            #candidate_list.append(candidate_name)

            #and begain tracking the candidate's voter count
           #candidate_votes[candidate_name]= 0

            #Then add a vote to that candidate's count
            #candidate_votes[candidate_name]= candidates_votes[candidates_name] + 1
#print(candidate_votes)            


