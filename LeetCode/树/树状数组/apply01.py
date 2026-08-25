# 单点更新 + 区间求值
class BinaryIndexedTree:
    def __init__(self, n):
        self.n = n
        # 树状数组需要从索引1开始, 不能传入0
        self.tree = [0] * (n + 1)

    def lowbit(self, x):
        return x & (-x)

    def update(self, index, val):
        while index <= self.n:
            self.tree[index] += val
            index += self.lowbit(index)

    def query(self, index):
        res = 0
        while index > 0:
            res += self.tree[index]
            index -= self.lowbit(index)
        return res

    def query_range(self, left, right):
        return self.query(right) - self.query(left - 1)


# 使用示例
def example_single_point_update():
    # 初始化数组 [1, 2, 3, 4, 5]
    arr = [1, 2, 3, 4, 5]
    n = len(arr)
    bit = BinaryIndexedTree(n)

    # 构建树状数组
    for i in range(n):
        bit.update(i + 1, arr[i])

    # 单点更新：将第3个元素加2
    bit.update(3, 2)  # arr[2] += 2

    # 查询区间和：查询[2,4]的和
    sum_range = bit.query_range(2, 4)
    print(f"区间[2,4]的和为：{sum_range}")  # 输出：区间[2,4]的和为：11
