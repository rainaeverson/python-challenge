#Total months in dataset
#Net total of profits/losses
#Changes in profits/losses
#Average change ^
#Greatest increase
#Greated decrease

#Import modules
import os
import csv

#Provide path
budget_data_csv = os.path.join("Resources", "budget_data.csv")

#Create empty lists



#Read in CSV file
with open(budget_data_csv) as file:

    reader = csv.reader(file, delimiter=',')
    header = next(reader)
    
    month =[]
    profitloss = []
    profit_change = []
    net_profit = []

    total_profitloss = 0
    max_decrease = 0
    max_increase = 0
    month_increase = ""
    month_decrease = ""

    firstrow = next(reader)
    profitloss.append(firstrow[1])
    total_profitloss = float(firstrow[1])
    row_index = 1


    for data in reader:

        profitloss.append(data[1])
    
        profit_change.append(float(profitloss[row_index]) - float(profitloss[row_index-1]))
            
        total_profitloss += float(data[1])
            
        #Find average change --- sum/no. of values
    #Loop through to find maximum increase and decrease with the month from the same row

        if float(profit_change[row_index - 1]) > max_increase:

            max_increase = float(profit_change[row_index - 1])
            month_increase = data[0]



        elif float(profit_change[row_index - 1]) < max_decrease:

            max_decrease = float(profit_change[row_index - 1])
            month_decrease = data[0]

        row_index = row_index + 1
        
    average_change = sum(profit_change) / len(profit_change)

    total_months = len(list(file))

print("")
print("Financial Analysis")
print("-------------------------------------")
print(f"Total Months: {total_months}")
print("")
print(f"Total: ${total_profitloss}")
print("")
print(f"Average Change: ${average_change}")
print("")
print(f"Greatest Increase in Profits = {month_increase} ${max_increase}")
print("")
print(f"Greatest Decrease in Profits = {month_decrease} ${max_decrease}")
print("")


#Export to text file
f = open("analysis.txt", "w")

print("", file=f)
print("Financial Analysis", file=f)
print("-------------------------------------", file=f)
print(f"Total Months: {total_months}", file=f)
print("", file=f)
print(f"Total: ${total_profitloss}", file=f)
print("", file=f)
print(f"Average Change: ${average_change}", file=f)
print("", file=f)
print(f"Greatest Increase in Profits = {month_increase} ${max_increase}", file=f)
print("", file=f)
print(f"Greatest Decrease in Profits = {month_decrease} ${max_decrease}", file=f)
print("", file=f)

f.close()