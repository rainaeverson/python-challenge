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



#Read in CSV file
with open(budget_data_csv) as file:

    reader = csv.reader(file, delimiter=',')
    header = next(reader)

    #Calculate the number of months
    total_months = len(list(file))
    print(f"Number of months: {total_months}")
    
    month =[]
    profitloss = []
    profit_change = [] 

    profitloss = 0
    total_profitloss = 0
    max_decrease = 0
    max_increase = 0
    month_increase = ""
    month_decrease = ""

    #Loop to calculate net profit and store changes
    
    for data in reader:

        month.append(file[0])
        profitloss.append(file[1])
        
        i = 0
        for i in reader:
            if i >= 1:
        
                profit_change.append(float(profitloss[i]) - float(profitloss[i-1]))
                
                total_profitloss += float(reader[1])
                i += 1

        #Find average change --- sum/no. of values

        average_change = (float(profit_change)) / total_months

    #Loop through to find maximum increase and decrease with the month from the same row
    o = 2
    for o in reader:
        if float(profitloss[o]) > float(profitloss[o-1]):

            max_increase = float(profitloss[o])
            month_increase = str(month[o])

            o += 1

        elif float(profitloss[o]) < float(profitloss[o-1]):

            max_decrease = float(profitloss[o])
            month_decrease = str(month[o])

            o += 1
        


    print(f"{month_increase} {max_increase}")
    print(f"{month_decrease} {max_decrease}")

    print(total_profitloss) 