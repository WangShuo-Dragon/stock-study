from stock.stock import Stock
from config.config import Config

def main():
    config = Config('.env')
    apikey = config.getEnvValue('apikey')
    stock = Stock(apikey)
    stock.test('data/result.xlsx')


if __name__ == '__main__':
    main()