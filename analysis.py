#Importing librariesimport osimport csv
#Initial variablesmonth_count = 0total = 0
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
with open(csvpath, 'r') as csvfile:	
    csvreader = csv.reader(csvfile, delimiter=',')	
    csv_header = next(csvreader)		
    
    for row in csvreader:	
        month_count = month_count + 1	
        total = total + row[1] 	

with open ('analysis .txt', 'w') as analysis:
    analysis.write("Financial Analysis")	
    analysis.write("----------------------------")	
    analysis.write(f"Total Months: {}")	
    analysis.write(f"Total: ${}")	
    analysis.write(f"Average Change: ${}")	
    analysis.write(f"Greatest Increase in Profits: {Aug-16} (${1862002})")	
    analysis.write(f"Greatest Decrease in Profits: {Feb-14} (${-1825558})")
