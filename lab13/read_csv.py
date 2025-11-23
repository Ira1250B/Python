import csv

file = "data.csv"

with open(r'C:\Users\bhoga\Downloads\data-1.csv', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)