class StockSpanner:
    def __init__(self):
        self.stack: list[tuple[int,int]] = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res
        
