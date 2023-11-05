import random
import sys

def main():
    problems = generate_integer(get_level())
    i = 0
    tries = 0
    score = 0
    while i < len(problems):
        try:
            result = int(input(f'{problems[i]} + {problems[i+1]} = '))
            if result == problems[i] + problems[i+1]:
                i = i+2
                score = score + 1
            else:
                tries = tries + 1
                print('EEE')
                if tries == 3:
                    print(f'{problems[i]} + {problems[i+1]} = {problems[i] + problems[i+1]}')
                    i = i+2
                    tries = 0
        except:
            pass
    print(f'Score: {score}')
    sys.exit(0)

def get_level():
    while True:
        try:
            level = int(input('Level: '))
            if level >= 1 and level <= 3:
                return level
        except ValueError:
            pass

def generate_integer(level):
    integers = []
    for _ in range(20):
        if level == 1:
            integers.append(random.randint(0,9))
        else:
            integers.append(random.randint(10**(level-1), 10**level))
    return integers

if __name__ == "__main__":
    main()
