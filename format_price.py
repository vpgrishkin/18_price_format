import sys
import locale
import re


NOT_AVALIABLE = 'Not available'
ACCURACY = 2


def get_price_from_argv_or_exit():
    if len(sys.argv) == 1:
        print('No arguments')
        sys.exit(1)
    else:
        return sys.argv[1]


def format_price(price):
    if not (isinstance(price, (int, float, str))):
        return NOT_AVALIABLE
    if isinstance(price, str):
        price = price.replace(' ', '').replace('\xa0', '')
    price_pattern = r'\d+([.,])?\d*$'
    if not re.match(price_pattern, str(price)):
        return NOT_AVALIABLE
    price_float = float(str(price).replace(',', '.'))
    locale.setlocale(locale.LC_ALL, '')
    format_price = locale.currency(price_float, symbol=False, grouping=True).replace('.00', '')
    if format_price == '' or format_price == '0':
        return NOT_AVALIABLE
    return format_price


if __name__ == '__main__':
    price = get_price_from_argv_or_exit()
    print(format_price(price))
    