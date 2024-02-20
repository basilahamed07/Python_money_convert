from forex_python.converter import CurrencyRates
import art

def get_exchange_rates(base_currency):
    c = CurrencyRates()
    rates = c.get_rates(base_currency)
    return rates

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    exchange_rate = c.get_rate(from_currency, to_currency)
    converted_amount = amount * exchange_rate
    return converted_amount

def display_supported_currencies():
    c = CurrencyRates()
    temp = []
    currencies = c.get_rates('USD').keys()
    print("Supported MONEY")
    for currency in currencies:
        temp += [currency]
    print("")
    print(temp)

def get_user_input():
    print("")
    amount_str = input("Enter the amount to convert: ")
    try:
        amount = float(amount_str)
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return get_user_input()

    from_currency = input("Enter the source Money code (e.g., USD): ").upper()
    return amount, from_currency

def main():
        print(art.text2art('MONEY CONVERCTOR :)'))
        print("")
        display_supported_currencies()

        amount, from_currency = get_user_input()

        rates = get_exchange_rates(from_currency)

        print(f"\nEquivalent amounts for {amount} {from_currency}:")
        for to_currency, rate in rates.items():
            converted_amount = convert_currency(amount, from_currency, to_currency)
            value = (f"{to_currency}: {converted_amount:.4f}")
            print("--------------------------------")
            print("|", from_currency, amount, "|", value, "|")

if __name__ == "__main__":
    main()
