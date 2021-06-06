import csv
import numpy as np
Coffee = []
sleep = []
with open("correlation.csv") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            Coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
correlation = np.corrcoef(Coffee,sleep) 
print("Correlation between Coffee in ml and sleep in hours in a week :-  \n--->",correlation[0,1])
