from typing import List


# 暴力解法, 超时了
class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def update(self, index: int, val: int) -> None:
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.nums[left : right + 1])


# 分块处理
class NumArray:
    def __init__(self, nums: List[int]):
        n = len(nums)
        size = int(n**0.5)
        sums = [0] * ((n + size - 1) // size)  # n/size 向上取整
        for i, num in enumerate(nums):
            sums[i // size] += num
        self.nums = nums
        self.sums = sums
        self.size = size

    def update(self, index: int, val: int) -> None:
        self.sums[index // self.size] += val - self.nums[index]
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        m = self.size
        b1, b2 = left // m, right // m
        if b1 == b2:  # 区间 [left, right] 在同一块中
            return sum(self.nums[left : right + 1])
        return sum(self.nums[left : (b1 + 1) * m]) + sum(self.sums[b1 + 1 : b2]) + sum(self.nums[b2 * m : right + 1])
