import csv

with open('people.csv') as entry: 
    for person in csv.reader(entry):
        print('Name: {}, Age: {}'.format(*person))