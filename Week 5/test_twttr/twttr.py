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


if __name__ == '__main__':
    main()