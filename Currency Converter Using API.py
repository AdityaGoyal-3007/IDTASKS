import requests
from_currency = input("Enter The Currency You Would Like To Convert From: ").upper()
to_currency = input("Enter The Currency You Would Like To Convert To: ").upper()
amount = float(input("Enter The Amount You Would Like To Convert: "))
resp = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={from_currency}&to={to_currency}")
print(f"{amount} {from_currency} Is Equal To {resp.json()['rates'][to_currency]} {to_currency}")
