import sys
from os.path import exists
import csv

def main():
    original = input_files()
    read = reader(original)
    final = renamer(read)
    writer(final)


def input_files():
    if len(sys.argv) != 3 or exists(sys.argv[1]) == False:
        sys.exit('Wrong Arguments')
    return sys.argv[1]

def reader(file):
    students = []
    with open (f'{file}', newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append({'name': row['name'], 'house': row['house']})
    return students

def renamer(list):
    final_students = []
    for student in list:
        last, first = student['name'].split(', ')
        final_students.append({'first': first, 'last': last, 'house': student['house']})
    return final_students

def writer(final):
    with open (f'{sys.argv[2]}', 'w', newline="") as file:
        writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in final:
            writer.writerow({'first': row['first'], 'last': row['last'], 'house': row['house']})

if __name__ == "__main__":
    main()