import sys
from os.path import exists
from tabulate import tabulate
import csv

def main():
    menu = read_file()
    prettify(menu)

def read_file():
    if len(sys.argv) != 2 or sys.argv[1].endswith('.csv') == False or exists(sys.argv[1]) == False:
        sys.exit('Arguments not valid')

    list = []
    with open (f'{sys.argv[1]}') as file:
        reader = csv.reader(file)
        for row in reader:
            list.append(row)

        return list

def prettify(list):
    print(tabulate(list, headers="firstrow",tablefmt="grid"))

if __name__ == "__main__":
    main()