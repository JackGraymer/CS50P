import re
import sys


def main():
    print(parse(input("HTML: ")))

def parse(s):
    pattern = r'<iframe .*?src=["\'](https?://(www\.)?youtube\.com/embed/([\w-]+))["\']'
    if match:= re.search(pattern, s):
        return(f'https://youtu.be/{match.group(3)}')

if __name__ == "__main__":
    main()