def main():
    name = input('Variable name? ')
    snake =''
    for char in name:
        if char.isupper():
            snake += '_' + char.lower()
        else:
            snake += char
    print(snake)

main()