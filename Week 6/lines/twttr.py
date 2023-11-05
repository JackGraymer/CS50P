def main():
    string = input('Type to shorten: ')
    print(shorten(string))

def shorten(string):
    vowels = "AaEeIiOoUu"
    short = ''
    for char in string:
        if char not in vowels:
            short += char
    return short


# calls only if run, not by a module

if __name__ == '__main__':
    main()