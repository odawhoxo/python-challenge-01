# Modules
import os
import csv

# Set path for file
csvpath = os.path.join(".", "Resources", "budget_data.csv")

# Open the CSV
with open(csvpath, encoding='utf') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)
    # Loop through looking for the video
    total_months = 0
    total_profits = 0
    for row in csvreader:
#print(row)
        total_months = total_months + 1 
        total_profits = float(row[1]) + total_profits
print(total_months)
print(total_profits)    