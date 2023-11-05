import validators

def main():
    email = input("What's your email address?").strip()
    print(validate_email(email))

def validate_email(email):
    if validators.email(email):
        return 'Valid'

    return 'Invalid'

if __name__ == '__main__':
    main()