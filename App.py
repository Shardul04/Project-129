import csv
import pandas as pd

file1 = 'dwarf.csv'
file2 = 'Star_Scrapper.csv'

dataset_1 = []
dataset_2 = []

with open(file1, 'r') as f:
    csv_reader = csv.reader(f)
    
    for i in csv_reader:
        dataset_2.append(i)
        
with open(file2, 'r') as f:
    csv_reader =csv.reader(f)
    
    for i in csv_reader:
        dataset_1.append(i)

headers_1 = dataset_1[0]
headers_2 = dataset_2[0]

planet_data_1 = dataset_1[1:]
planet_data_2 = dataset_2[1:]

headers = headers_1+headers_2

planet_data =[]

for i in planet_data_1:
    planet_data.append(i)

for j in planet_data_2:
    planet_data.append(j)

with open("Merged_dataset.csv", 'w') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)   
    csvwriter.writerows(planet_data)
