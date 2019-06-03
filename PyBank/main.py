#PyBank
import os
import sys
import csv
#open file and write to file
budget_data = os.path.join(".", "budget_data.csv")
financial_analysis = os.path.join(".", "financial_analysis.txt")
with open (budget_data, "r", newline="") as filehandle:
    next(filehandle)
    csvreader = csv.reader(filehandle)
    # loop
    total_months = 0 
    total_net_amount = 0 
    monthly_changes = 0 
    prev_month_amount = 0 
    current_month_amount = 0 
    diff_current_prev = 0  
    greatest_increase = 0 
    greatest_decrease = 0 
    current_month = ""
    greatest_increase_month = ""
    greatest_decrease_month = ""
    for row in csvreader:
        total_months += 1
        current_month = row[0]
        current_month_amount = float(row[1])
        total_net_amount += current_month_amount
        diff_current_prev = current_month_amount - prev_month_amount 
        if (csvreader.line_num != 1):
            monthly_changes += diff_current_prev
        if (diff_current_prev > greatest_increase):
            greatest_increase = diff_current_prev
            greatest_increase_month = current_month
        if (diff_current_prev < greatest_decrease):
            greatest_decrease = diff_current_prev
            greatest_decrease_month = current_month
        prev_month_amount = current_month_amount
#calculate average change
average_change = monthly_changes/(total_months-1)
#print file
with open(financial_analysis, "w+") as filehandle:
    filehandle.write("Financial Analysis\n")
    filehandle.write("-" *32 + "\n")
    filehandle.write(f"Total Months: {total_months: .0f}\n")
    filehandle.write(f"Total: ${total_net_amount: .0f}\n")
    filehandle.write(f"Average Change: ${average_change: .2f}\n")
    filehandle.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase: .0f})\n")
    filehandle.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease: .0f})\n")
# print screen
with open(financial_analysis, "r") as filehandle:
    print(filehandle.read())
