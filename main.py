import os
from bs4 import BeautifulSoup

class Trade:
    def __init__(self, type, price, crypto, total, time):
        self.type = type
        self.price = float(price)
        self.crypto = float(crypto)
        self.total = float(total)
        self.time = time

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
print(sum(t.total if t.type == 'Buy' else 0 for t in trades))
print(sum(t.total if t.type == 'Sell' else 0 for t in trades))


