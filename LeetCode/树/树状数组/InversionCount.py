"""
逆序对数
给定一个数组 `a[0],a[1],a[2]...`
一对下标 `(i,j)`，如果满足：
>
> i <j 并且 a [i] > a [j]
> 就称为一对逆序对。
> 逆序对数：整个数组里面，这样的逆序对总数量。
"""

# 1. 暴力枚举
# arr = [3, 1, 2]
# cnt = 0
# n = len(arr)
# for i in range(n):
#     for j in range(i + 1, n):
#         if arr[i] > arr[j]:
#             cnt += 1
# print(cnt)


# 2. 树状数组
class BIT:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def lowbit(self, x):
        return x & -x

    def update(self, idx, val):
        while idx <= self.n:
            self.tree[idx] += val
            idx += self.lowbit(idx)

    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= self.lowbit(idx)
        return res


def count_inv_left(arr):
    if not arr:
        return 0
    rank = {v: i for i, v in enumerate(sorted(set(arr)), 1)}  # 下标从1开始
    bit = BIT(len(rank))
    total = 0
    for i, num in enumerate(arr):  # i = 左侧已插入的个数
        rk = rank[num]
        total += i - bit.query(rk)  # 左边比 num 大的个数
        bit.update(rk, 1)
    return total


print(count_inv_left([5, 2, 6, 1, 3]))
