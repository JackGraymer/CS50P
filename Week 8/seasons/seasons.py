from datetime import date, datetime
import inflect
import re
import sys
p = inflect.engine()

def main():
    birth_date = input("Date of Birth: ").strip()
    birth_date = birth(birth_date)
    return print((difference(birth_date)))


def birth(bdate):
    pattern = r'^(?:19|20)\d\d-(?:(?:0[1-9]|1[0-2])-(?:0[1-9]|1\d|2[0-8])|(?:0[13-9]|1[0-2])-(?:29|30)|(?:0[13578]|1[02])-31)$'
    if bdate := re.match(pattern, bdate):
        return str(bdate.group(0))
    else:
        sys.exit("Invalid input")

def difference(birthdate):
        date_difference = datetime.strptime(str(date.today()), "%Y-%m-%d") - datetime.strptime((birthdate), "%Y-%m-%d")
        minutes = date_difference.days * 24 * 60
        words = p.number_to_words(minutes, andword="").capitalize()
        return  words + ' minutes'

if __name__ == "__main__":
    main()
