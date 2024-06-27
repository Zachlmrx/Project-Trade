import requests
import json

def main():
    key = '5e413e0da973db0013e32165d8bf8066-db650c27639854a773560e12c3a77b6a'
    accountid = '101-002-29348741-001'
    stream = 'stream-fxpractice.oanda.com'
    instruments = 'USD_CAD,WTICO_USD'

    params = {'instruments': instruments} 
    bearer = f'Bearer {key}'
    headers = {'Authorization': bearer}

    response = requests.get(f'https://{stream}/v3/accounts/{accountid}/pricing/stream', params=params, headers=headers, stream=True)

    print (response)
    with response:
        for line in response.iter_lines(decode_unicode=True):
            data = json.loads(line)
            print(data)


if __name__ == '__main__':
    main()
