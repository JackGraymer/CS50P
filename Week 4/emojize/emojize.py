import emoji
def main():
    str = input('Input: ')
    print(emoji.emojize(str, language='alias'))

main()