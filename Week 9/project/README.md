# CURRENCY CONVERTER

#### Video Demo: <[URL HERE](https://youtu.be/O8xrM37EL88)>

#### Description:

This project is a comprehensive currency converter that allows users to convert between a wide range of different currencies. It leverages real-time exchange rates to provide the most accurate conversions possible.

The project is structured into three main Python files:

- `main.py`: This is the main script that runs the currency converter. It handles user input and output, and orchestrates the overall flow of the program. It prompts the user for input, validates it, and calls the appropriate functions based on the user's input. This file also contains the core functionality of the currency converter. It includes functions for fetching real-time exchange rates from an external API, converting between different currencies, and handling exceptions. It also includes helper functions for validating user input and formatting output.

- `test_project.py`: This file contains the unit tests for the project. It tests the functions in `main.py` to ensure they are working correctly. The tests cover a range of scenarios, including valid and invalid user input, and different currency conversion cases.

- `currency-list.json`: This file contains a list of currencies that the converter supports. It is used to validate user input and to save on API calls by avoiding fetching the list of currencies from the API every time.

During the development of this project, I faced a key decision: whether to use real-time exchange rates or fixed exchange rates. I decided to use real-time exchange rates because they provide more accurate conversions. However, this decision introduced a level of complexity, as the output of the program can change based on the current exchange rates.

Despite this challenge, I am proud of this project because it is user-friendly, robust, and provides accurate currency conversions. I have put a lot of effort into ensuring the code is clean, well-structured, and thoroughly tested. I hope you find it useful and I look forward to receiving your feedback!
