import os
import csv

#Call out the path to the intial data file

csv_path = os.path.join("Resources", "budget_data.csv")

#Call out the path for the file containin the calculated data

calculated_data_file = os.path.join("Budget_Calculations.txt")

# Analyze budget data

def analyze_budget_data(csv_path):

    # Create variables

    Month_Total = 0
    Total_Profit = 0
    Previous_Profit = 0
    Total_Profit_Change = 0
    Profit_Change_List = []
    Month_Change_List = []

    # Read the initial data file

    with open(csv_path, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",")
        next(csvreader)

        # Work through rows of data, skipping the header

        for row in csvreader:
            Month_Total += 1
            Current_Profit = int(row[1])
            Total_Profit += Current_Profit

            # Calculate change in profit. Checking the previous profit to see if is zero or not

            if Previous_Profit != 0:
                Profit_Change = Current_Profit - Previous_Profit
                Profit_Change_List.append(Profit_Change)
                Month_Change_List.append(row[0])
                Total_Profit_Change += Profit_Change

            # Update previous profit

            Previous_Profit = Current_Profit

        # Calculate average change

        Avg_Change = Total_Profit_Change / (Month_Total - 1)

        # Find maximum increase and decrease in Profits

        Max_Increase = max(Profit_Change_List)
        Max_Increase_Month = Month_Change_List[Profit_Change_List.index(Max_Increase)]
        Max_Decrease = min(Profit_Change_List)
        Max_Decrease_Month = Month_Change_List[Profit_Change_List.index(Max_Decrease)]

    # Generate Summary Table

    Summary_Table = (
        f"\nFinancial Analysis\n"
        f"--------------------------------------------------------------------\n"
        f"Total Months: {Month_Total}\n"
        f"Total: ${Total_Profit}\n"
        f"Average Change: ${Avg_Change:.2f}\n"
        f"Greatest Increase in Profits: {Max_Increase_Month} (${Max_Increase})\n"
        f"Greatest Decrease in Profits: {Max_Decrease_Month} (${Max_Decrease})\n"
    )

    # Print the anaylized data

    print(Summary_Table)

    # Write the Summary Table to a file

    with open(calculated_data_file, "w") as resultfile:
        resultfile.write(Summary_Table)

# Call a function analyze_budget_data() to analyze the budget data

analyze_budget_data(csv_path)