import requests
import json

def get_eth():
    url = 'https://www.alphavantage.co/query?function=CRYPTO_INTRADAY&symbol=ETH&market=USD&interval=5min&apikey=demo'
    r = requests.get(url)
    data = r.json()
    with open("data_file.json", "w") as write_file:
        json.dump(data, write_file,indent=4)
    with open("data_file.json", "r") as read_file:
        data = json.load(read_file)
    for key1, walues1 in data.items():
        if key1 == 'Time Series Crypto (5min)':
            for key2, walues2 in walues1.items():
                key_list = list(walues1.keys())
                max_key = max(key_list)
                if key2 == max_key:
                    for k,w in walues2.items():
                        if k == '4. close':
                            need_value = w
    return need_value

def get_btc():
    import requests
    url = 'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol=BTC&market=CNY&apikey=demo'
    r = requests.get(url)
    data = r.json()
    with open("data2_file.json", "w") as write_file:
        json.dump(data, write_file,indent=4)
    with open("data2_file.json", "r") as read_file:
        data = json.load(read_file)
    for key1, walues1 in data.items():
        if key1 == 'Time Series (Digital Currency Daily)':
            for key2, walues2 in walues1.items():
                key_list = list(walues1.keys())
                max_key = max(key_list)
                if key2 == max_key:
                    for k,w in walues2.items():
                        if k == '4b. close (USD)':
                            need_value = w
    return need_value
