# First, import the os module
# This will allow us to create file paths across operating systems
import os

#Module for reading CSV files
import csv

#call out path to initial data file
csv_path = os.path.join("Resources", "budget_data.csv")

#Create variable for the output text file
output_file = 'output_results.txt'

#Specify the file path for saving the output text file
output_file_path = os.path.join('Analysis', output_file)

# Analyze budget data
def analyze_budget_data(csv_path):
     # Create variables
     total_months = 0
     net_total = 0
     previous_profit_loss = 0
     total_change = 0
     greatest_increase = {"date": "", "amount": 0}
     greatest_decrease = {"date": "", "amount": 0}

     # Read through csv file, skipping the header row
     with open(csv_path, 'r') as csvfile:
          # Read the initial CSV file
          csvreader = csv.reader(csvfile, delimiter= ',')
          next(csvreader)

          for row in csvreader:
               date = row[0]
               profit_loss = int(row[1])

               # Add to the total number of months variable. Then, add each month's profit/loss to the running net_total:
               total_months +=1
               # net_total = net_total + profit_loss
               net_total += profit_loss

               # Calculate the change in profit for each month        
               if previous_profit_loss != 0:
                    change = profit_loss - previous_profit_loss
               # Add the change in each month to a new variable that sums all the monthly changes
                    total_change += change

                    # Calculate greatest increase in profits (date and amount) over the entire period
                    if change > greatest_increase["amount"]:
                         greatest_increase["date"] = date
                         greatest_increase["amount"] = change
                    # Calculate the greatest decrease in profits (date and amount) over the entire period
                    elif change < greatest_decrease["amount"]:
                         greatest_decrease["date"] = date
                         greatest_decrease["amount"] = change           
               
               # Update previous profit_loss for the next iteration of the loop
               previous_profit_loss = profit_loss
     print(f"------test----   {total_change}")

     # Calculate the average change in profit_loss over the entire period
     average_change = total_change / (total_months - 1)

     with open(output_file_path, 'w') as output_file:
          # Write the string to the file
          output_file.write("Financial Analysis\n")
          output_file.write("------------------\n")
          output_file.write(f"Total Months: {total_months}\n")
          output_file.write(f"Total: ${net_total}\n")
          output_file.write(f"Average Change: ${average_change:.2f}\n")
          output_file.write(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n")
          output_file.write(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n")
               
     # Print the results to the console
     print("Financial Analysis")
     print(f"Total Months: {total_months}") 
     print(f"Total: ${net_total}")
     print(f"Average Change: ${average_change:.2f}")
     print(f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})")
     print(f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})")

# Call the function with the specified CSV file path
analyze_budget_data(csv_path)
