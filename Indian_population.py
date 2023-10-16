import csv
import matplotlib.pyplot as plt

population={}

with open('Dataset/population-estimates_csv.csv',newline='') as csvfile:
    
    data=csv.DictReader(csvfile)
    
    
    for row in data:
        if row['Region']=='India':
            population[row['Year']]=float(row['Population'])

plt.bar(population.keys(),population.values())
plt.show()