import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        size = len(nums)
        q = [(-nums[i], i) for i in range(size)]
        heapq.heapify(q)

        for _ in range(k - 1):
            heapq.heappop(q)

        return -q[0][0]

    def findKthLargest1(self, nums: List[int], k: int) -> int:
        res = []
        for num in nums:
            if len(res) < k:
                heapq.heappush(res, num)
            elif num > res[0]:
                heapq.heappop(res)
                heapq.heappush(res, num)
                
        return heapq.heappop(res)


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 2))
    print(s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
    print(s.findKthLargest([3, 2, 1, 5, 6, 4], 1))
    print(s.findKthLargest([1], 1))
    print(s.findKthLargest([1, 2], 2))
    print(s.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))
    print(s.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))
    print(s.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
    print(s.findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
