class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def build(self, arr):
        for i in range(len(arr)):
            self.update(i + 1, arr[i])

    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)

    # 树状数组的求和
    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res