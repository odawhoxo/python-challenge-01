#!/usr/bin/env python
# coding: utf-8

# # PyBank 
# 

# In[108]:


import os
import csv

csv_path = os.path.join(".", "Resources", "budget_data.csv")
#csv_path
csv_output_path = os.path.join(".","budget_analysis.txt")
#csv_output_path

total_months = 0
total_net = 0
previous_net = 0
profit_loss_changes = []

greatest_increase_date = ""
greatest_increase_amount = 0
greatest_decrease_date = ""
greatest_decrease_amount = 0

with open(csv_path) as budget_data:
    csv_reader = csv.reader(budget_data)
#    print(csv_reader)
    csv_header = next(csv_reader)    
#   print(csv_header)
    
    for row in csv_reader:
        total_months = total_months + 1
        total_net = int(row[1]) + total_net
#       print(row)
        profit_loss_change = int(row[1]) - previous_net
        profit_loss_changes.append(profit_loss_change)
        previous_net = int(row[1])
        if profit_loss_change > greatest_increase_amount:
            greatest_increase_amount = profit_loss_change
            greatest_increase_date = row[0]
        elif profit_loss_change < greatest_decrease_amount:
            greatest_decrease_amount = profit_loss_change
            greatest_decrease_date = row[0]
profit_loss_changes.pop(0)
average_change = sum(profit_loss_changes) / len(profit_loss_changes)

print("Financial Analysis")
print("-------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_net}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")

with open(csv_output_path,'w') as output_file:
    output_file.write("Financial Analysis \n")
    output_file.write("-------------------------------------------\n")
    output_file.write(f"Total Months: {total_months}\n")
    output_file.write(f"Total: ${total_net}\n")
    output_file.write(f"Average Change: ${average_change:.2f}\n")
    output_file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase_amount})\n")
    output_file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease_amount})")
                 

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $22564198
# Average Change: $-8311.11
# Greatest Increase in Profits: Aug-16 ($1862002)
# Greatest Decrease in Profits: Feb-14 ($-1825558)
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# In[ ]:





# In[ ]:




