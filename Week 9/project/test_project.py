import requests
from unittest.mock import patch
import project
import json
from tabulate import tabulate


def test_api_key():
    assert requests.get(
        'https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_PDrHnMrW5GyRg4xmmjMLJBSHpa9iO0xvcRdvqEPk').status_code == 200


def test_currency_list():
    with open('./currency_list.json', 'r') as json_file:
        data = json.load(json_file)
        expected_output = tabulate(
            data['Currency List'], headers='keys', tablefmt='mixed_grid')
    assert project.currency_list() == expected_output


def test_instructions():
    expected_output = tabulate({
        'Instructions': 'input',
        'Display the instructions': "help",
        'Display the currency list': "list",
        'Display the currency rate': "rate",
        'Convert a currency': "convert",
        'Exit the program': "exit"
    }.items(), headers='firstrow', tablefmt='heavy_grid')
    assert project.instructions() == expected_output


def test_input_main():
    with patch('builtins.input', return_value='exit'):
        assert project.input_main() == None
