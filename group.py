import csv
import matplotlib.pyplot as plt

Countries = ["Brunei Darussalam", "Cambodia", "Indonesia", "Lao People's Democratic Republic", "Malaysia", "Myanmar", "Philippines", "Singapore", "Thailand", "Viet Nam"]

ASEAN_POPULATION={}
curr={}
with open('Dataset/population-estimates_csv.csv',newline='') as csvfile:
    data=csv.DictReader(csvfile)
    
    for row in data:
        if row['Region'] in Countries and row['Year'] not in ASEAN_POPULATION and 2004<=int(row['Year'])<=2014:
            curr[row["Year"]]=float(row['Population'])
            ASEAN_POPULATION[row['Region']]=curr
        elif row['Region'] in Countries and row['Year'] in ASEAN_POPULATION:
            curr[row["Year"]]=float(row['Population'])
            ASEAN_POPULATION[row['Region']]=curr
l=[]
b=list(ASEAN_POPULATION.values())
for i in range(len(b)):
    print(b[i].values())
    l.append(list(b[i].values()))
