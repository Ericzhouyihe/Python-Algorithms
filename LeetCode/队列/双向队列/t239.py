import heapq
from typing import List


class Solution:
    # 优先队列
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)
        res = [-q[0][0]]
        for i in range(k, len(nums)):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k:
                heapq.heappop(q)
            res.append(-q[0][0])
        return res

    # 循环列表更新数据, 然后用max()计算最大值, 实际上等同二重循环, 超时了
    def maxSlidingWindow1(self, nums: List[int], k: int) -> List[int]:
        lst = nums[:k]
        max_value = max(lst)
        res = [max_value,]
        for i in range(k, len(nums)):
            lst[i % len(lst)] = nums[i]
            res.append(max(lst))
        return res

# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))
    print(s.maxSlidingWindow([1, -1], 1))
