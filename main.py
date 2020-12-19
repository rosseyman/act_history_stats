import os
from bs4 import BeautifulSoup
from datetime import datetime


class Trade:
    def __init__(self, type, price, crypto, total, time):
        self.type = type
        self.price = float(price)
        self.crypto = float(crypto)
        self.total = float(total)
        self.time = datetime.strptime(time, '%Y-%m-%d %H:%M:%S')

    def __repr__(self):
        return f'{self.type=} {self.price=} {self.crypto=} {self.total=} {self.time=}'


files = os.listdir(os.path.dirname(os.path.abspath(__file__)) + '/trade_history')
trades = []
for file in files:

    if file.endswith('.html'):
        print(file)
        f = open(os.path.dirname(os.path.abspath(__file__)) + '\\trade_history\\' + file)
        soup = BeautifulSoup(f.read(), 'html.parser')
        for row in soup.find_all('tr')[1:]:
            cells = [c.text for c in row.find_all('td')]

            trade = Trade(cells[0], cells[1], cells[2], cells[3], cells[4])
            trades.append(trade)

start_date = datetime.strptime('2020-03-01 00:00:00', '%Y-%m-%d %H:%M:%S')
end_date = datetime.strptime('2021-02-28 00:00:00', '%Y-%m-%d %H:%M:%S')
total_buys = sum([t.total if t.type == 'Buy' and start_date < t.time < end_date else 0 for t in trades])
total_sells = sum([t.total if t.type == 'Sell' and start_date < t.time < end_date else 0 for t in trades])
print(f'Profit: {total_sells - total_buys}, Total Sells: {total_sells}, Total Buys: {total_buys}')
print(f'Number of Trades: {sum(1 if start_date < t.time < end_date else 0  for t in trades)}')


