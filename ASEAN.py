import csv
import matplotlib.pyplot as plt

Countries = ["Brunei Darussalam", "Cambodia", "Indonesia", "Lao People's Democratic Republic", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Viet Nam"]

ASEAN_POPULATION={}

with open('Dataset/population-estimates_csv.csv',newline='') as csvfile:
    data=csv.DictReader(csvfile)
    
    for row in data:
        if row['Region']in Countries and row['Year']=='2014':
            ASEAN_POPULATION[row["Region"]]=float(row['Population'])

print(ASEAN_POPULATION)
plt.bar(ASEAN_POPULATION.keys(),ASEAN_POPULATION.values())
plt.show()