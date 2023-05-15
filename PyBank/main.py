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
budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

#Create empty lists
month =[]
profitloss = []
profit_change = []

total_profitloss = 0
#Read in CSV file
with open(budget_data_csv) as file:

    reader = csv.reader(file, delimiter=',')
    header = next(reader)

    #Calculate the number of months
    total_months = len(list(file))
    print(f"Number of months: {total_months}")
        

    row = 0
    
    for data in profitloss:

        month.append(data[0])
        profitloss.append(data[1])

        final_data = profitloss[row]

        if row >= 0:
        
            #profit_change.append(float(profitloss[row]) - float(profitloss[row-1]))
            total_profitloss += float(data[1])

        row += 1

    print(total_profitloss)