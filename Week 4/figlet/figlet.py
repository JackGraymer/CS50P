from pyfiglet import Figlet
import sys
import random

'''
implement a program that:

    - Expects zero or two command-line arguments:
        - Zero if the user would like to output text in a random font.
        - Two if the user would like to output text in a specific font, in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
    - Prompts the user for a str of text.
    - Outputs that text in the desired font.

If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program should exit via sys.exit with an error message.'''

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        text = input('Input: ')
        f = Figlet(font=random.choice(fonts))
        print (f.renderText(text))


    elif len(sys.argv) == 3:
        if sys.argv[1] == '-f' or sys.argv[1] == '--font':
            if sys.argv[2] in fonts:
                text = input('Input: ')
                f = Figlet(font=sys.argv[2])
                print (f.renderText(text))
            else:
                sys.exit('Wrong Second arguments')
        else:
            sys.exit('Wrong First arguments')

    else:
        sys.exit('Bad input, program aborted')


        """ f = Figlet(font='slant')
        print(sys.argv[0])
        print (f.renderText(text)) """

main()