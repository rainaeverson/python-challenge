#import modules
import os
import csv

budget_data_csv = os.path.join("..", "Resources", "budget_data.csv")

with open(budget_data_csv) as file:

    reader = csv.reader(file, delimiter=',')
    header = next(reader)

    for row in reader:
        month = reader[0]
        profitloss = float(reader[1])
    
