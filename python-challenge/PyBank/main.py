import pandas as pd
import os

# Load the dataset
file_path = 'python-challenge/PyBank/resources_pybank/budget_data.csv'
data = pd.read_csv(file_path)

# Calculate the total number of months
total_months = len(data['Date'])

# Calculate the net total amount of "Profit/Losses"
total_profit_losses = data['Profit/Losses'].sum()

# Calculate the changes in "Profit/Losses" and the average of those changes
data['Change'] = data['Profit/Losses'].diff()
average_change = data['Change'].mean()

# Find the greatest increase and decrease in profits
greatest_increase = data['Change'].max()
greatest_decrease = data['Change'].min()

greatest_increase_date = data.loc[data['Change'] == greatest_increase, 'Date'].values[0]
greatest_decrease_date = data.loc[data['Change'] == greatest_decrease, 'Date'].values[0]

# Print the results
print("Financial Analysis")
print("----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit_losses}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

# Ensure the directory exists
output_dir = 'PyBank_Analysis'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the output file path
output_path = os.path.join(output_dir, 'financial_analysis.txt')

# Export the results to a text file
with open(output_path, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("----------------------------\n")
    file.write(f"Total Months: {total_months}\n")
    file.write(f"Total: ${total_profit_losses}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")