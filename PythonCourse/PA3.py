import requests
import json


def get_currency_difference():
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        usd_rate = data['Valute']['USD']['Value']
        eur_rate = data['Valute']['EUR']['Value']

        difference = usd_rate / eur_rate

        print(f"Курс доллара: {usd_rate} руб.")
        print(f"Курс евро: {eur_rate} руб.")
        print(f"Доллар отличается от евро в {difference:.2f} раз")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка запроса: {e}")
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
    except KeyError as e:
        print(f"Ошибка доступа к данным: {e}")


get_currency_difference()
