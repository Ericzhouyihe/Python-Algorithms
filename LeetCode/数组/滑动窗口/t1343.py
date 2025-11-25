# 1343. 大小为 K 且平均值大于等于阈值的子数组数目
# 给你一个整数数组 arr 和两个整数 k 和 threshold 。
# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = sum = 0
        index = k - 1
        for i in range(k - 1):
            sum += arr[i]
        while index < len(arr):
            sum += arr[index]
            if sum / k >= threshold:
                ans += 1
            sum -= arr[index - k + 1]
            index+=1
        return ans
