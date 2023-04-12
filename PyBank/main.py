# First we will import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading csv files
import csv

# Path to collect data from the Resource folder
budget_data_filepath = os.path.join("Resources", "budget_data.csv")

# Loop through the csv file
with open(budget_data_filepath, newline="") as budgetfile:
    csv_reader = csv.reader(budgetfile, delimiter=',')
    
    # store the header row
    csv_header = next(csv_reader)
    # print(f"Header: {csv_header}")
    
    # find net amount of profit and loss
    months = []
    profit_loss = []

    # read each row of data after header
    for rows in csv_reader:
        months.append(rows[0])
        profit_loss.append(int(rows[1]))

    # find revenue change
    revenue_change = []

    for i in range(1, len(profit_loss)):
        revenue_change.append((int(profit_loss[i]) - int(profit_loss[i-1])))

    # calculate average revenue change
    revenue_average_change = sum(revenue_change) / len(revenue_change)
    revenue_average = round(revenue_average_change, 2)

    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)

    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print Results
    print ("Financial Analysis")

    print("-----------------------------------")
    print ("Total Months:" + str(total_months))
    print("Total:" + "$" + str(sum(profit_loss)))
    print ("Average Change:" + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")")
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")")

    # output to a text file
    output_filepath = os.path.join("Analysis", "Results.txt")
    outputfile = open(output_filepath,"w")
    outputfile.write("Financial Analysis" + "\n")
    outputfile.write("-----------------------------------" + "\n")
    outputfile.write("total months: " + str(total_months) + "\n")
    outputfile.write("Total: " + "$" + str(sum(profit_loss)) + "\n")
    outputfile.write("Average change: " + "$" + str(revenue_average) + "\n")
    outputfile.write("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "($" + str(greatest_increase) + ")\n")
    outputfile.write("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "($" + str(greatest_decrease) + ")\n")
    outputfile.close()