import inflect
p = inflect.engine()

def main():
    names = []
    while True:
        try:
            names.append(input('Name:'))
        except EOFError:
            return print('\nAdieu, adieu, to ' + p.join(names))


main()