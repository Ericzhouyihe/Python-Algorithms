class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))

        return res


# 测试
if __name__ == "__main__":
    stock = StockSpanner()
    print(stock.next(100))
    print(stock.next(80))
    print(stock.next(60))
    print(stock.next(70))
    print(stock.next(60))
    print(stock.next(75))
    print(stock.next(85))
