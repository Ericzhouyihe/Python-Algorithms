# 子数组最大平均数
from typing import List

class Solution:
    def findMaxAverage( nums: List[int], k: int) -> float:
        maxTotal = total = sum(nums[:k])

        for i in range(k, len(nums)):
            total = total + nums[i] - nums[i - k]
            maxTotal = max(maxTotal, total)

        return maxTotal / k


print(Solution.findMaxAverage([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
