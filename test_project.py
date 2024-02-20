from unittest.mock import patch
from project import get_exchange_rates, convert_currency, display_supported_currencies, get_user_input, main

def test_get_exchange_rates():
    with patch('project.CurrencyRates') as mock_currency_rates:
        mock_instance = mock_currency_rates.return_value
        mock_instance.get_rates.return_value = {'EUR': 0.85, 'GBP': 0.75}

        rates = get_exchange_rates('USD')

        mock_instance.get_rates.assert_called_once_with('USD')
        assert rates == {'EUR': 0.85, 'GBP': 0.75}

def test_convert_currency():
    with patch('project.CurrencyRates') as mock_currency_rates:
        mock_instance = mock_currency_rates.return_value
        mock_instance.get_rate.return_value = 0.85

        amount = 100
        converted_amount = convert_currency(amount, 'USD', 'EUR')

        mock_instance.get_rate.assert_called_once_with('USD', 'EUR')
        assert converted_amount == 85.0

def test_display_supported_currencies(capsys):
    with patch('project.CurrencyRates') as mock_currency_rates:
        mock_instance = mock_currency_rates.return_value
        mock_instance.get_rates.return_value = {'EUR': 0.85, 'GBP': 0.75}

        display_supported_currencies()

        captured = capsys.readouterr()
        expected_output = "Supported MONEY\n\n['EUR', 'GBP']\n"

        assert captured.out == expected_output

if __name__ == '__main__':
    pytest.main(['-v', 'test_project.py'])
