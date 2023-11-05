import sys
from os.path import exists
def main():

    if len(sys.argv) < 2:
            sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif '.py' not in sys.argv[1]:
        sys.exit('Not a Python file')
    elif exists(sys.argv[1]) == False:
        sys.exit('File does not exist')
    else:
        open_file(sys.argv[1])

def open_file(file):
    with open(f'{file}') as file:
        lines = file.readlines()
    total = 0

    for line in lines:
        line = line.strip()
        if len(line) !=0 and line[0] != '#':
            total = total + 1
    print(total)

if __name__ == "__main__":
    main()