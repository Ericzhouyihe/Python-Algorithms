import heapq
from typing import List
from collections import deque


# 解法超时了...
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        n = len(nums)
        if k > n:
            res.append(max(nums))
            return res
        d = deque([nums[i] for i in range(k)])
        res.append(max(d))
        for i in range(k, n):
            d.popleft()
            d.append(nums[i])
            res.append(max(d))

        return res

    # 单调队列, 将最大的放在最前面就行, 将前面小的都弹出去
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ans = []

        for i, x in enumerate(nums):
            if q and q[0] <= i - k:
                q.popleft()

            while q and nums[q[-1]] <= x:
                q.pop()

            q.append(i)

            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans

    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            ans.append(-q[0][0])

        return ans


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow1([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow2([1, 3, -1, -3, 5, 3, 6, 7], 3))

    # 输出：3 + 3 + (-1) + (-3) + 5 + 3 = 15
    # 解释：子数组 [1, 3, -1] 对应的元素和为 3 。
    # 子数组 [3, -1, -3] 对应的元素和为 3 。
    # 子数组 [-1, -3, 5] 对应的元素和为 -1 。
    # 子数组 [-3, 5, 3] 对应的元素和为 5 。
    # 子数组 [5, 3, 6] 对应的元素和为 14 。
    # 子数组 [3, 6, 7] 对应的元素和为 16 。
    # 最大的元素和为 16 。
