import requests
import logging
from datetime import datetime
from typing import Dict, List, Tuple, Optional

timestamps: List = []
stock_price: List = []

logging.basicConfig(filename='monitor.log',
                    format='%(asctime)s %(message)s', level=logging.INFO)


def get_stocks_data(stocks_code: str) -> Dict:

    result: requests.models.Response = requests.get(
        f'https://www.stockexchangeofmauritius.com/interactive-graph?market=official&filename={stocks_code}')

    result_json: Dict = result.json()
    logging.info(f'Data fetched for stock {stocks_code} from SEMDEX')

    return result_json


def add_to_lists(result_json: Dict):

    for elem in result_json['data']:
        timestamps.append(elem[0] / 1000)
        stock_price.append(elem[1])


def send_telegram_message(bot_message: str, bot_token: str, bot_chatID: str):

    send_text: str = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}'
    logging.info('SEMDEX Bot: Message Sent to Telegram')

    response: requests.models.Response = requests.get(send_text)


def notify_stocks():

    import time

    stock_diff: int

    if (stock_price[-1] > stock_price[-2]):

        stock_diff = stock_price[-1] - stock_price[-2]
        send_increase = send_telegram_message(
            f'Current value is {stock_price[-1]} at {time.ctime(timestamps[-1])}. Stocks rose by {stock_diff}.')

    elif (stock_price[-1] < stock_price[-2]):

        stock_diff = stock_price[-2] - stock_price[-1]
        send_increase = send_telegram_message(
            f'Current value is {stock_price[-1]} at {time.ctime(timestamps[-1])}. Stocks fell by {stock_diff}.')

    else:

        send_increase = send_telegram_message(
            f'Current value is {stock_price[-1]} at {time.ctime(timestamps[-1])}. Stocks showed no change')


def notify_at_buy(bot_token: str, bot_chatID: str):

    import time

    if (stock_price[-1] == 0.01):
        send_telegram_message(
            f'Current value is {stock_price[-1]} at {time.ctime(timestamps[-1])}.', bot_token, bot_chatID)


def main() -> None:
    import json

    with open('config.json', 'rb') as config_file:
        config = json.load(config_file)

    bot_token: str = config['bot_token']
    bot_chatID: str = config['chat_id']
    stocks_id: str = config['stocks_id']

    result = get_stocks_data(stocks_id)

    add_to_lists(result)

    # notify_stocks()

    notify_at_buy(bot_token, bot_chatID)


if __name__ == "__main__":
    main()
