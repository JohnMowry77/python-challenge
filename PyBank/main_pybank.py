import csv
import os

file_to_load = os.path.join("Resources", "budget_data.csv")

total_months = 0
month_of_change = []
net_change_list = []
greatest_increase = ["", 0] #allows for a very large positive number,
greatest_decrease = ["", 9999999999999999999] #allows for a very large negative number
total_net = 0 #set total net profit to zero 
with open(file_to_load) as financial_data:
   reader = csv.reader(financial_data) #read the file
   header = next(reader) #skip header row
   first_row = next(reader) 
   #print(first_row) prints the first row after the header
   total_months += 1 #total months equals total months +1
   total_net += int(first_row[1]) #total_net equals total_net + turns first_row into number
   prev_net = int(first_row[1])
   for row in reader:  #each row is its own list
       #print(row[0]) #Print the date only in this example
       total_months += 1 #total months = total months + 1
       total_net += int(row[1]) #total_net = total net + convert 
       net_change = int(row[1]) - prev_net
       prev_net = int(row[1])
       net_change_list += [net_change] 
       month_of_change += [row[0]]
       if net_change > greatest_increase[1]: #us if statement net_change > greatest increase 
           greatest_increase[0] = row[0]  
           greatest_increase[1] = net_change
       if net_change < greatest_decrease[1]:
           greatest_decrease[0] = row[0]
           greatest_decrease[1] = net_change
net_monthly_avg = sum(net_change_list) / len(net_change_list)
output = (
   f"Financial Analysis\n"
   f"----------------------------\n"  #print space in between 
   f"Total Months: {total_months}\n" #print total months = the number of months move to next line of code
   f"Total: ${total_net}\n"#print total = the number of months...
   f"Average  Change: ${net_monthly_avg:.2f}\n"
   f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)

#specify the file to write to
output_path=os.path.join("Resources", "pybank_analysis.txt")
#open the file using "write" mode. Specifiy the variable to hold the contents
#output = (
   #f"Financial Analysis\n"
   #f"----------------------------\n"  #print space in between 
   #f"Total Months: {total_months}\n" #print total months = the number of months move to next line of code
   #f"Total: ${total_net}\n"#print total = the number of months...
   #f"Average  Change: ${net_monthly_avg:.2f}\n"
   #f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
   #f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n")
print(output)
#writer is a function of the csv module imported on line 1
with open(output_path, 'w', newline='') as csvfile:
    #initialize csv.writer
    #csvwriter= csv.writer(csvfile, delimiter=',')
    csvwriter= csv.writer(csvfile)
    csvwriter.writerow(['Financial Analysis']) #write row financial analysis to new txt file which python will read
    csvwriter.writerow(['Total Months']) #write row total months to new txt file which python will read
    csvwriter.writerow(['Total'])
    csvwriter.writerow(['Average Change'])
    csvwriter.writerow(['Greatest Increase in Profits'])
    csvwriter.writerow(['Greatest Decrease in Profits'])
    