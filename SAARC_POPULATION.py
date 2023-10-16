import csv
import matplotlib.pyplot as plt

saarc_countries = ["Afghanistan", "Bangladesh", "Bhutan", "India", "Maldives", "Nepal", "Pakistan", "Sri Lanka"]

SAARC_POPULATION={}

with open('Dataset/population-estimates_csv.csv',newline='') as csvfile:
    data=csv.DictReader(csvfile)
    
    for row in data:
        if row['Region']in saarc_countries and row['Year'] not in SAARC_POPULATION:
            SAARC_POPULATION[row["Year"]]=float(row['Population'])
        elif row['Region']in saarc_countries:
            SAARC_POPULATION[row["Year"]]+=float(row['Population'])

print(SAARC_POPULATION)
plt.bar(SAARC_POPULATION.keys(),SAARC_POPULATION.values())
plt.xticks(rotation=90)
plt.show()