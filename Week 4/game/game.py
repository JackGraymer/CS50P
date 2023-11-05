import random

def main():
    level = 0
    guess = 0
    while True:
        try:
            level = int(input('Level:'))
            if level > 0:
                break
        except ValueError:
            pass
    solution = random.randint(1, level)

    while guess != solution:
        #while guess < 1:
        try:
            guess = int(input('Guess: '))
        except ValueError:
            pass
        if guess < solution:
            print('Too small!')
        elif guess > solution:
            print('Too large!')

    print('Just right!')

if __name__ == "__main__":
    main()