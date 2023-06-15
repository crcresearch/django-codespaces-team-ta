# WRITING CSV FILES (with Dictionaries)
import csv
data = [
    {
        'name': 'David',
        'location': 'ND'
    },
    {
        'name': 'Sam',
        'location': 'ND'
    },
    {
        'name': 'Sarah',
        'location': 'Home'
    }
]

file_out = open('persons.csv', 'w')
csv_out = csv.DictWriter(file_out, ['name', 'location'])

csv_out.writeheader()
csv_out.writerows(data)
file_out.close()
