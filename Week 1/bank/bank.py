def main():
    str = input('Greeting? ').lower().strip()
    if  'hello' in str:
        print('$0')
    elif str[0] == 'h':
        print('$20')
    else:
        print('$100')

main()