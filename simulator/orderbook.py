class OrderBook:
    def __init__(self):
        self.bids = []
        self.asks = []

    def add_order(self, price, volume, side):
        order = {'price': price, 'volume': volume}
        if side == 'bid':
            self.bids.append(order)
            self.bids = sorted(self.bids, key=lambda x: -x['price'])
        else:
            self.asks.append(order)
            self.asks = sorted(self.asks, key=lambda x: x['price'])

    def match_orders(self):
        trades = []
        while self.bids and self.asks and self.bids[0]['price'] >= self.asks[0]['price']:
            trade_volume = min(self.bids[0]['volume'], self.asks[0]['volume'])
            trade_price = (self.bids[0]['price'] + self.asks[0]['price']) / 2
            trades.append({'price': trade_price, 'volume': trade_volume})

            self.bids[0]['volume'] -= trade_volume
            self.asks[0]['volume'] -= trade_volume

            if self.bids[0]['volume'] == 0:
                self.bids.pop(0)
            if self.asks[0]['volume'] == 0:
                self.asks.pop(0)
        return trades
