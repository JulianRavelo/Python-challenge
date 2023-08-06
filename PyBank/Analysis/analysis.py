#Importing libraries
import os
import csv

#Initial variables
month_count = 0
total = 0
changes = []
months = []
previous_row = 0
total_change = 0
minimum = 0
maximum = 0
minimum_month ="" 
maximum_month = ""

# Look for csv data
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Open csv
with open(csvpath, 'r') as csvfile:	
    csvreader = csv.reader(csvfile, delimiter=',')	
    csv_header = next(csvreader)		
    # Read csv file and calculate total months and total profit/losses
    for row in csvreader:	
        month_count = month_count + 1	
        total = total + int(row[1])
        # Comparing previous value with current to populate Changes list
        if previous_row != 0:
            changes.append(int(row[1])-int(previous_row)) 
              
        previous_row = row[1]
        months.append(row[0])

    # Calculate total and then average by running through list 'Changes'   
    for value in changes:
        total_change = total_change + int(value)
        
# Calculation of average, maximum and minimum in list Changes
average = round(total_change / (month_count-1),2)
maximum = changes.index(max(changes))+1
maximum_month = months [maximum]
minimum = changes.index(min(changes))+1
minimum_month = months [minimum]

# Write on txt file
with open ('analysis.txt', 'w') as analysis:
    analysis.write("Financial Analysis\n \n \n----------------------------\n \n")	
    analysis.write(f"Total Months: {month_count}\n \n")	
    analysis.write(f"Total: ${total}\n \n")	
    analysis.write(f"Average Change: ${average}\n \n")	
    analysis.write(f"Greatest Increase in Profits: {maximum_month} (${max(changes)})\n \n")	
    analysis.write(f"Greatest Decrease in Profits: {minimum_month} (${min(changes)})")
