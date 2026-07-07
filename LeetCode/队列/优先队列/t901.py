# 暴力解法
# class StockSpanner:

#     def __init__(self):
#         self.lst = []

#     def next(self, price: int) -> int:
#         if len(self.lst) < 1:
#             self.lst.append((price, 1))
#             return 1
#         num = 1
#         index = len(self.lst) - 1
#         p, l = self.lst[index]
#         while index >= 0 and price >= p:
#             num += l
#             index -= l
#             p, l = self.lst[index]
#         self.lst.append((price, num))
#         return num

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

# 单调栈
from cmath import inf


class StockSpanner:

    def __init__(self):
        self.lst = [(-1, inf)]
        self.idx = -1

    def next(self, price: int) -> int:
        self.idx += 1
        while price >= self.lst[-1][1]:
            self.lst.pop()
        self.lst.append((self.idx, price))
        return self.idx - self.lst[-2][0]

# 测试
if __name__ == '__main__':
    obj = StockSpanner()
    print(obj.next(100))
    print(obj.next(80))
    print(obj.next(60))
    print(obj.next(70))
    print(obj.next(60))
    print(obj.next(75))
    print(obj.next(85))
