# 区间更新 + 单点求值
class RangeUpdateBIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def lowbit(self, x):
        return x and (-x)

    def update(self, index, val):
        while index < self.n:
            self.tree[index] += val
            index += self.lowbit(index)

    # 单点求值
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res

    # 区间更新
    def range_update(self, left, right, val):
        self.update(left, val)
        self.update(right + 1, -val)
