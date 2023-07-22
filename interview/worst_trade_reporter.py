class PnLCalculator:
    def __init__(self):
        self._prices = dict[str, int]()
        self._trades = dict[str, list[tuple[int, str, int, int]]]()
    
    def process_trade(self, trade_id: int, instrument_id: str, buy_sell: str, price: int, volume: int):
        if instrument_id not in self._trades:
            self._trades[instrument_id] = []
        self._trades[instrument_id].append((trade_id, buy_sell, price, volume))

    def process_price_update(self, instrument_id: str, price):
        self._prices[instrument_id] = price

    def output_worst_trade(self, instrument_id: str):
        res = (-1, -1) # id, pnL
        trades = self._trades.get(instrument_id, [])
        for id, buy_sell, price, volume in trades:
            diff = (price - self._prices[instrument_id]) * (1 if buy_sell == 'SELL' else -1)
            pnl = diff * volume
            if pnl <= res[1]:
                res = (id, pnl)
        
        return res[0] if res[0] != -1 else "NO BAD TRADES"