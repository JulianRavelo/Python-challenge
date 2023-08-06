# Importing libraries
import os
import csv

# Initial variables
count = 0
candidates = []
candidate0 = 0
candidate1 = 0
candidate2 = 0
percentage0 = 0
percentage1 = 0
percentage2 = 0
winner = 0
winnername =""

# Look for csv data
csvpath = os.path.join('Resources', 'election_data.csv')

# Open csv
with open(csvpath, 'r') as csvfile:	
    csvreader = csv.reader(csvfile, delimiter=',')	
    csv_header = next(csvreader)		
    # Read csv file and sum up total votes
    for row in csvreader:	
        count = count + 1	

        # Creating list of candidates and counting votes per candidate
        if row[2] not in candidates:
            candidates.append(row[2])
        if row[2] == candidates[0]:
            candidate0 = candidate0 + 1
        elif row[2] == candidates[1]:
            candidate1 = candidate1 + 1
        else:
            candidate2 = candidate2 + 1

# Calculating percentages of votes per candidate
percentage0 = round((candidate0 / (candidate0+candidate1+candidate2))*100,3)
percentage1 = round((candidate1 / (candidate0+candidate1+candidate2))*100,3)
percentage2 = round((candidate2 / (candidate0+candidate1+candidate2))*100,3)

# Selecting winner
if candidate0 > candidate1 and candidate0 > candidate2:
    winner = candidate0
    winnername = candidates[0]
elif candidate1 > candidate0 and candidate1 > candidate2:
    winner = candidate1
    winnername = candidates[1]
else:
    winner = candidate2
    winnername = candidates[2]

# Printing results
print("Election Results\n----------------------------")	
print(f"Total Votes: {count}")	
print(f"{candidates[0]}: {percentage0}% ({candidate0})")	
print(f"{candidates[1]}: {percentage1}% ({candidate1})")
print(f"{candidates[2]}: {percentage2}% ({candidate2})")
print("----------------------------")
print(f"Winner: {winnername}")
print("----------------------------")

# Write on txt file
txtpath = os.path.join('Analysis', 'analysis.txt')
with open (txtpath, 'w') as analysis:
    analysis.write(f"Election Results \n \n----------------------------\n \n")	
    analysis.write(f"Total Votes: {count} \n \n----------------------------\n \n")
    analysis.write(f"{candidates[0]}: {percentage0}% ({candidate0}) \n \n")	
    analysis.write(f"{candidates[1]}: {percentage1}% ({candidate1}) \n \n")	
    analysis.write(f"{candidates[2]}: {percentage2}% ({candidate2}) \n \n")		
    analysis.write("----------------------------\n \n")
    analysis.write(f"Winner: {winnername} \n \n")	
    analysis.write("----------------------------")
