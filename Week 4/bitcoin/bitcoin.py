import sys
import requests

def main():
    bitcoins = input_bitcoins()
    print(f"${round(price() * bitcoins, 4):,}")

def input_bitcoins():
    try:
        bitcoins = float(sys.argv[1])
    except (ValueError, IndexError):
        sys.exit('Value error, not a float')
    return bitcoins



def price():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        r = float(r["bpi"]['USD']['rate'].replace(',',''))
        return r
    except requests.RequestException:
        pass

if __name__ == '__main__':
    main()