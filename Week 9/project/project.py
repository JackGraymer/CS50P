import requests
import json
from tabulate import tabulate

key = 'fca_live_PDrHnMrW5GyRg4xmmjMLJBSHpa9iO0xvcRdvqEPk'
url = 'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_PDrHnMrW5GyRg4xmmjMLJBSHpa9iO0xvcRdvqEPk'


def main():
    print('Welcome to the currency converter')
    print(instructions())
    input_main()
    return


def currency_list():
    with open('./currency_list.json', 'r') as json_file:
        data = json.load(json_file)
        return (tabulate(data['Currency List'],
                         headers='keys', tablefmt='mixed_grid'))


def instructions(instructions=None):
    if instructions is None:
        instructions = {
            'Instructions': 'input',
            'Display the instructions': "help",
            'Display the currency list': "list",
            'Display the currency rate': "rate",
            'Convert a currency': "convert",
            'Exit the program': "exit"
        }
    return (tabulate(instructions.items(), headers='firstrow', tablefmt='heavy_grid'))


def input_main():
    while True:
        user_input = input('Enter a command: ').lower()
        if user_input == 'help':
            print(instructions())
        elif user_input == 'list':
            print(currency_list())
        elif user_input == 'rate':
            print(get_currency_rate())
        elif user_input == 'convert':
            print(get_currency_conversion())
        elif user_input == 'exit':
            break
        else:
            print('Invalid command')


def get_currency_rate():  # continue here
    tinstructions = {
        'Instructions': 'input',
        'If no input is given, the default currency is USD': '""',
        'For all rates of a currency, enter the currency code eg:': 'EUR',
        '2 inputs, first is currency from, second is currency to eg:': 'AUD USD',
        'For more than 2 rates, separate the second input with a comma eg:': 'AUD USD,EUR,GBP'
    }

    print(instructions(tinstructions))

    user_input = input('Enter a Rate command: ').upper()
    try:
        if user_input == '' or len(user_input) == 3:  # Continue Here
            print(get_default_rate(user_input))
        elif len(user_input) > 3:
            print(get_single_several_rate(user_input))
    except:
        print('Invalid command')


def get_default_rate(user_input='USD'):
    if user_input == '':
        user_input = 'USD'
    res = requests.get(f'{url}&base_currency={user_input}').json()
    return tabulate(res['data'].items(), headers=[user_input, 'Rate'], tablefmt='fancy_grid')


def get_single_several_rate(user_input):
    user_input = user_input.split(' ')
    print(user_input[0], user_input[1])
    res = requests.get(
        f'{url}&base_currency={user_input[0]}&currencies={user_input[1]}').json()
    return tabulate(res['data'].items(), headers=[user_input[0], 'Rate'], tablefmt='fancy_grid')


def get_currency_conversion():
    tinstructions = {
        'Conversion Instructions': 'input',
        'Enter the amount to be converted': '100',
        'Enter the currency to be converted from': 'USD',
        'Enter the currency to be converted to': 'AUD'
    }

    print(instructions(tinstructions))

    amount = input('Enter the amount to be converted: ')
    from_currency = input('Enter the currency to be converted from: ').upper()
    to_currency = input('Enter the currency to be converted to: ').upper()
    try:
        res = requests.get(
            f'{url}&base_currency={from_currency}&currencies={to_currency}').json()
        for i in res['data']:
            res['data'][i] = float(res['data'][i]) * float(amount)
        return tabulate(res['data'].items(), headers=[from_currency, amount], tablefmt='fancy_grid')
    except:
        print('Invalid command')


if __name__ == '__main__':
    main()
