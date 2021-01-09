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
  
    #Use for loop to Fill Lists
    for row in (csvreader):
        candidates_dup.append(row[2]) #add candidates name to candidates_dup list
    candidate_list = set(candidates_dup) #use set property to remove duplicate from candidate dup list
    candidate_list = list(candidate_list) #convert to list
    number_candidates= len(candidate_list) #how many candidates
    #print(number_candidates) Print number_candidates  result is 4

    #Find the total number of votes cast
    #For row in csvreader:
    #total_votes += 1 #can use this to find total votes, set total_votes to zero
    total_votes = len(candidates_dup) #returns the total_votes using len function
    #print(total_votes) #print total votes 35210001
    #store candidates and votes to dictonary use {}
    #candidates= {'candidate1': Khan, 'candidate2': Correy, 'candidate3': Li, 'candidate4': OTooley}

    #results_total=dict(collections.counter(candidate_list))

    pypoll = {} #call the dict pypoll
    candidates= {"candidate1": "Khan", "candidate2": "Correy", "candidate3": "Li", "candidate3": "OTooley"}
    #print(candidates)
    #for x,y in candidates.items():
        #print(f"{x},{y}")

    #for loop to itereate through dict
    #for i in range(len(results_total)):
        #candidates_list.append(results_total/int(len(candidate_list)))
    #print(candidates_votes)    
    for i in range(number_candidates): #range function returns a sequence of numbers, starting from 0 by default
        #and increments by 1 (by default), and ends at a specified number
        pypoll [candidate_list[i]]= candidates_dup.count(candidate_list [i]) #use pypoll dict and set candidate_list to candidates+dup.count list
        print(candidate_list[i]) #print the name in candidate_list 
        print(float(pypoll[candidate_list[i]])/total_votes*100) #print decimal #perecentage of votes each candidate won
        #convert row 41 to percent???
        print(total_votes)
        print(pypoll[candidate_list[i]]) #print total number of votes each candidate won
        print("--------------------------")
        #khan= 0
        #correy= 0
        #li = 0
        #oTooley= 0
        #print winner
        #use string function and max to find the candidates with most votes from candidate_list[i]
        #the winner of the election based on popular vote
    print("Winner: " + str(max(pypoll)))
    poll_win= 0
    #for x, y in candidates.items():
       # if y > poll_win:
            #poll_win_count = y
            #poll_win_name = x
    #print (f"{poll_win_name}-{poll_win_count}")
    #error if y > pol_win: Typeerror: '>' not supported between instances of 'str' and 'int'
        #compary candidates to other candidates


output = (          
    f"Election Results\n"
    f"----------------------------\n"  #print space in between 
    f"Total Votes: {total_votes}\n"
    f"----------------------------\n"
    #f"candidate: {candidates}\n"
    #f"khan: {candidate_list[i]}\n"
    #f"Khan: 63.000% (2218231) #how to get this in f string? 
    #f"Correy: 20.000% (704200) \n"
    #f"Li: 14.000% (492940)
    #f"O'Tooley: 3.000% (105630)
    f"----------------------------\n" 
    #f"Winner:  + str(max({pypoll})))\n"
    f"----------------------------\n") 
print(output)
output_path = os.path.join("Resources", "election_results.txt")
#writer is a function of the csv module imported on line 1
with open(output_path, 'w', newline='') as csvfile:
    #initialize csv.writer
    #csvwriter= csv.writer(csvfile, delimiter=',')
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(['Election Results']) #write row election results to new txt file which python will read
    csvwriter.writerow(['Total Votes']) #write row total votes to new txt file which python will read
    csvwriter.writerow(['Khan'])
    csvwriter.writerow(['Correy'])
    csvwriter.writerow(['Li'])
    csvwriter.writerow(['OTooley'])
    csvwriter.writerow(['Winner'])


       

   