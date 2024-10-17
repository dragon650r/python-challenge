# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r"C:\Users\josej\OneDrive\Desktop\Module3Homework\Resources\budget_data.csv"  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Check if the output directory exists, if not, create it
output_directory = os.path.dirname(file_to_output)
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Define variables to track the financial data
total_months = 0
total_profit_losses = 0
profit_changes = []
previous_profit = None
greatest_increase = ("", 0)  # (date, amount)
greatest_decrease = ("", float("inf"))  # (date, amount)

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Process each row of data
    for row in reader:
        # Track the total months
        total_months += 1
        
        # Track the profit/losses
        date = row[0]
        profit_losses = int(row[1])
        total_profit_losses += profit_losses

        # Track the net change
        if previous_profit is not None:
            change = profit_losses - previous_profit
            profit_changes.append(change)

            # Calculate the greatest increase in profits (month and amount)
            if change > greatest_increase[1]:
                greatest_increase = (date, change)

            # Calculate the greatest decrease in losses (month and amount)
            if change < greatest_decrease[1]:
                greatest_decrease = (date, change)

        previous_profit = profit_losses  # Update previous profit to current

# Calculate the average net change across the months
average_change = sum(profit_changes) / len(profit_changes) if profit_changes else 0

# Generate the output summary
analysis_report = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_profit_losses}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)

# Print the output
print(analysis_report)

# Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(analysis_report)