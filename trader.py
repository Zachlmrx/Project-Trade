import requests
import json

def main():

    f = open('/Users/Zach/Desktop/config.json')
    data = json.load(f)
    
    key = data['key']
    accountid = data['accountid']
    stream = data['stream']
    instruments = data['instruments']

    params = {'instruments': instruments} 
    bearer = f'Bearer {key}'
    headers = {'Authorization': bearer}

    response = requests.get(f'https://{stream}/v3/accounts/{accountid}/pricing/stream', params=params, headers=headers, stream=True)

    print (response)
    with response:
        for line in response.iter_lines(decode_unicode=True):
            data = json.loads(line)
            try: 
                print(data['bids'][0]['price'], data['instrument'])
            except:
                ...
            


if __name__ == '__main__':
    main()
