import requests
import json
import yaml
import os

class Trader:

    def __init__(self):
        
        yamlfile = 'C:\\Users\\iCan Student\\OneDrive - Riverside School Board\\Desktop\\config.yaml'
        with open(yamlfile, 'r') as file:
           data = yaml.safe_load(file)

        self.accountid = data['accountid']
        self.stream_api = data['stream']
        self.instruments = data['instruments']
        self.trades_api = data['trades']

        self.params = {'instruments': self.instruments} 
        self.bearer = f"Bearer {data['key']}"
        self.headers = {'Authorization': self.bearer}
        print(self.accountid)

    def main(self):
        # self.stream()
        # self.orders()
        ...

    def stream(self):
        
        response = requests.get(f'https://{self.stream_api}/v3/accounts/{self.accountid}/pricing/stream', params=self.params, headers=self.headers, stream=True)

        print (response)
        with response:
            for line in response.iter_lines(decode_unicode=True):
                data = json.loads(line)
                try: 
                    print(data['bids'][0]['price'], data['instrument'])
                except:
                    ...

    def orders(self):
        response = requests.get(f'https://{self.trades_api}/v3/accounts/{self.accountid}/orders', params=self.params, headers=self.headers)
        orders = (json.loads(response.content))
        order = orders['orders'][0]
        order_id = order['id']
        instrument = order['instrument']
        units = order['units']
        price = float(order['price'])
        print(f'my order id is {order_id} for instrument {instrument} with {units} units at price {price}.')
        sell_price, buy_price = self.pricing(instrument)
        print(f'sell: {sell_price}, buy: {buy_price}')
        buy_distance = price - buy_price
        print(buy_distance)

    def pricing(self, instrument): 
        params = {
            'instruments': instrument,
        }
        response = requests.get(f'https://{self.trades_api}/v3/accounts/{self.accountid}/pricing', params=params, headers=self.headers)
        prices = (json.loads(response.content))
        sell_price = float(prices['prices'][0]['closeoutBid'])
        buy_price = float(prices['prices'][0]['closeoutAsk'])
        return sell_price, buy_price

if __name__ == '__main__':
    Trader().main()
