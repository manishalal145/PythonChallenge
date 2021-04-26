# Importing dependencies
import os
import csv

# Set path for file
bank_csv = os.path.join("PyBank", "Resources", "budget_data.csv")

# Open and read csv
with open(bank_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first
    csv_header = next(csv_file)

    #  Declarations and list to store data
    total_months = 0
    total = 0
    revenue =[]
    month = []
    total_change = []
    

    # Read through each row of data after the header
    for row in csv_reader:
        
        # The total number of months included in the dataset
        total_months = total_months + 1
        
        # The net total amount of "Profit/Losses" over the entire period
        total = total + int(row[1])

        # Filling the revenue and month array with the csv file data
        revenue.append(row[1])
        month.append(row[0])

# The average of the changes in "Profit/Losses" over the entire period
i = 0
for i in range(0, len(revenue) - 1):
    change = int(revenue[i+1]) - int(revenue[i])
    total_change.append(change)
average_change = round(sum(total_change)/len(total_change),2)

# The greatest increase in profits
max_profit = max(total_change)
x = total_change.index(max_profit)
month_profit = month[x+1]

# The greatest decrease in losses
min_losses = min(total_change)
a = total_change.index(min_losses)
month_losses = month[a+1]

# To terminal
print("Financial Analysis")
print("------------------------------------")
print(f"Total months: {total_months}")
print(f"Total: ${total}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {month_profit} (${max_profit})")
print(f"Greatest Decrease in Profits: {month_losses} (${min_losses})")

# Create analysis file
bank_file = os.path.join("PyBank", "Analysis", "bank_data.txt")
with open (bank_file, 'w') as outputfile:
    outputfile.write(f"Financial Analysis\n")
    outputfile.write("-------------------------\n")
    outputfile.write(f"Total months: {total_months}\n")
    outputfile.write(f"Total: ${total}\n")
    outputfile.write(f"Average Change: ${average_change}\n")
    outputfile.write(f"Greatest Increase in Profits: {month_profit} (${max_profit})\n")
    outputfile.write(f"Greatest Decrease in Profits: {month_losses} (${min_losses})\n")