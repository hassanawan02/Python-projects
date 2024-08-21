import requests

currencyFrom = input("Skriv inn valuta fra: ")
currencyTo = input("Skriv inn valuta til: ")
amount = input("Skriv inn antall: ")

valutaData = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={currencyFrom}&to={currencyTo}")

sum = valutaData.json()["rates"][currencyTo]

print(f"{amount} {currencyFrom} er {sum} {currencyTo}")
