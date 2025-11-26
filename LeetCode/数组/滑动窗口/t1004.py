import bisect
from typing import List

"""
最大连续1的个数III
找到最多翻转k个0后能够得到的最长连续1的子数组长度

参数:
   nums: 由0和1组成的数组
   k: 最多可以翻转的0的个数

返回值:
   翻转最多k个0后能得到的最长连续1的子数组长度
"""
class Solution:
    def longestOnes1(self, nums: List[int], k: int) -> int:

        n = len(nums)
        # 构建前缀和数组，p[i]表示前i个元素中0的个数
        p = [0]
        for num in nums:
            p.append(p[-1] + 1 - num)

        ans = 0
        # 遍历右端点，使用二分查找确定满足条件的最左端点
        for right in range(n):
            # 查找第一个使得区间[left, right]内0的个数不超过k的位置
            left = bisect.bisect_left(p, p[right + 1] - k)
            ans = max(ans, right - left + 1)

        return ans

    def longestOnes2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left = lsum = rsum = 0
        ans = 0

        # 使用滑动窗口技术找到最长子数组
        for right in range(n):
            # 累计当前窗口中0的个数
            rsum += 1 - nums[right]

            # 当窗口中0的个数超过k时，移动左指针缩小窗口
            while lsum < rsum - k:
                lsum += 1 - nums[left]
                left += 1

            # 更新最大窗口长度
            ans = max(ans, right - left + 1)

        return ans
