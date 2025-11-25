from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        left, right = 0, 1
        res = 0
        while right < n:
            if nums[right] > nums[right - 1]:
                right += 1
            else:
                res = max(res, right - left)
                left = right
                right += 1
        res = max(res, right - left)
        return res
