def main():
    vowels = "AaEeIiOoUu"
    string = input('Type to shorten: ')
    short = ''
    for char in string:
        if char not in vowels:
            short += char
    print(short)

main()