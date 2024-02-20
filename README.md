# Fast_Money_Converter
#### Video Demo:  <https://youtu.be/_UtNErCikq4>
________________________________________________________________________________________________________________________________________________________________________________

## Description:

  The Money Converter is a Python-based application intended to work with consistent money changes. With a clear order line interface, clients can easily change over sums between various monetary standards, using constant trade rates obtained from a dependable Programming interface.
________________________________________________________________________________________________________________________________________________________________________________
TODO
## Table of Contents

- [Project_file_structure](#Project_file_structure)
- [Libraries](#libararies)
- [Installing_Libraries](#Installing_Libraries)
- [Usage](#usage)
- [function](#function)
- [pytest](#pytest) ________________________________________________________________________________________________________________________________________________________________________________

## Project_file_structure :

 - project.py
 - test_project.py
 - requirements.txt
 - README.md
________________________________________________________________________________________________________________________________________________________________________________

## __Libraries__

__forex-python__ : The forex-python library is a Python module that provides a simple and easy-to-use interface for fetching exchange rates. [(Readmore)](http://forex-python.readthedocs.io/en/latest/usage.html)

__ART__ : ASCII art is also known as "computer text art". It involves the smart placement of typed special characters or letters to make a visual shape that is spread over multiple lines of text.[(Readmore)](https://pypi.org/project/art/)

__PYTEST__ : Pytest is a testing framework for Python that makes it easy to write and execute unit tests. It is widely used in the Python community due to its simplicity, powerful features, and ability to integrate with other testing tools. [(Readmore)](https://docs.pytest.org/en/7.1.x/contents.html)
________________________________________________________________________________________________________________________________________________________________________________

## **Installing_Libraries**
there is a a __requirements.txt__ file that has all the libraries used.

and simply can be install by this pip command:

```pip install -r requirements.txt```

_________________________________________________________________________________________________________________________________________________________________________________
## __Usage__

```python project.py```
```
──╼ $python3 project.py
 __  __   ___   _   _  _____ __   __   ____   ___   _   _ __     __ _____  ____    ____  _____   ___   ____      __
|  \/  | / _ \ | \ | || ____|\ \ / /  / ___| / _ \ | \ | |\ \   / /| ____||  _ \  / ___||_   _| / _ \ |  _ \   _ \ \
| |\/| || | | ||  \| ||  _|   \ V /  | |    | | | ||  \| | \ \ / / |  _|  | |_) || |      | |  | | | || |_) | (_) | |
| |  | || |_| || |\  || |___   | |   | |___ | |_| || |\  |  \ V /  | |___ |  _ < | |___   | |  | |_| ||  _ <   _  | |
|_|  |_| \___/ |_| \_||_____|  |_|    \____| \___/ |_| \_|   \_/   |_____||_| \_\ \____|  |_|   \___/ |_| \_\ (_) | |
                                                                                                                 /_/


Supported MONEY

['EUR', 'JPY', 'BGN', 'CZK', 'DKK', 'GBP', 'HUF', 'PLN', 'RON', 'SEK', 'CHF', 'ISK', 'NOK', 'TRY', 'AUD', 'BRL', 'CAD', 'CNY', 'HKD', 'IDR', 'INR', 'KRW', 'MXN', 'MYR', 'NZD', 'PHP', 'SGD', 'THB', 'ZAR']

Enter the amount to convert: ```
```
After that You can enter the .amount of money you want to convert
```
Enter the amount to convert: 10000.32
Enter the source Money code (e.g., USD):
```
after you enter the some amount you will redirect to the source of the money that mean your current Money country.
```
Enter the amount to convert: 10000.32
Enter the source Money code (e.g., USD): INR

Equivalent amounts for 10000.32 INR:
--------------------------------
| INR 10000.32 | EUR: 112.5604 |
--------------------------------
| INR 10000.32 | USD: 120.1020 |
--------------------------------
| INR 10000.32 | JPY: 18230.2894 |
--------------------------------
| INR 10000.32 | BGN: 220.1457 |
--------------------------------
| INR 10000.32 | CZK: 2766.8482 |
--------------------------------
| INR 10000.32 | DKK: 839.6784 |
--------------------------------
| INR 10000.32 | GBP: 98.1021 |
--------------------------------
| INR 10000.32 | HUF: 42457.7991 |
--------------------------------
| INR 10000.32 | PLN: 498.4176 |
--------------------------------
| INR 10000.32 | RON: 559.5380 |
--------------------------------
| INR 10000.32 | SEK: 1306.8267 |
--------------------------------
| INR 10000.32 | CHF: 108.6884 |
--------------------------------
| INR 10000.32 | ISK: 17255.5159 |
--------------------------------
| INR 10000.32 | NOK: 1336.8804 |
--------------------------------
| INR 10000.32 | TRY: 3433.5550 |
--------------------------------
| INR 10000.32 | AUD: 188.4487 |
--------------------------------
| INR 10000.32 | BRL: 592.0567 |
--------------------------------
| INR 10000.32 | CAD: 166.0717 |
--------------------------------
| INR 10000.32 | CNY: 875.6527 |
--------------------------------
| INR 10000.32 | HKD: 937.7298 |
--------------------------------
| INR 10000.32 | IDR: 1885601.2855 |
--------------------------------
| INR 10000.32 | KRW: 159128.9495 |
--------------------------------
| INR 10000.32 | MXN: 2125.3663 |
--------------------------------
| INR 10000.32 | MYR: 565.4361 |
--------------------------------
| INR 10000.32 | NZD: 204.2072 |
--------------------------------
| INR 10000.32 | PHP: 6735.8420 |
--------------------------------
| INR 10000.32 | SGD: 163.4378 |
--------------------------------
| INR 10000.32 | THB: 4323.1089 |
--------------------------------
| INR 10000.32 | ZAR: 2251.4903 |
```
then you enter the source country money that will show the all the other country money convert at the time so that will reduce the time and save the time :)

## __function__

the project.py contains 5 functions including the main function.

### get_exchange_rates(base_currency) __function__ :
  -Takes a base_currency as input.
  -Uses the CurrencyRates class from forex_python to get exchange rates for the specified base currency.
  -Returns a dictionary of exchange rates

### convert_currency(amount, from_currency, to_currency) __function__ :

  -Takes amount, from_currency, and to_currency as inputs.
  -Uses the CurrencyRates class to get the exchange rate between the source and target currencies.
  -Calculates the converted amount.
  -Returns the converted amount

### display_supported_currencies() __function__ :
  -Uses the CurrencyRates class to get exchange rates for the base currency (USD in this case).
  -Prints a list of supported currencies.

### get_user_input() __function__ :
  -Takes no arguments.
  -Asks the user to input the amount and source currency code.
  -Validates the input to ensure the amount is a valid number.
  -Returns the amount and source currency code.

### main() __function__ :
  -The main function that orchestrates the program.
  -Prints an ASCII art title using the art library.
  -Calls display_supported_currencies() to show the supported currencies.
  -Gets user input for the amount and source currency using get_user_input().
  -Calls get_exchange_rates() to get exchange rates.
  -Iterates over the exchange rates, converts the amount for each target currency, and prints the results.

## __pytest__:
  - I am completed three pytest in this code they are
        -test_get_exchange_rates(),
        -test_convert_currency(),
        -test_display_supported_currencies(capsys).

### Author : Basil Ahamed
