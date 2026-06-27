from collections import defaultdict
from typing import Counter, List
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [item[0] for item in heapq.nlargest(k, [(num, nums.count(num)) for num in set(nums)], key=lambda x: x[1])]

    def topKFrequent1(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)  # 统计频率
        max_cnt = max(cnt.values())  # 最大频率
        print(cnt)

        """
        collections 模块中的一个特殊字典，作用是：
        当访问一个不存在的 key 时，自动用 list()（即空列表 []）作为默认值，而不是抛出 KeyError。
        """
        bucket = defaultdict(list)
        ans = []

        for x, c in cnt.items():  # 将相同频率的数字放入一个桶中
            bucket[c].append(x)

        for freq in range(max_cnt, 0, -1):  # 拿到前 k 个频率最高的数字
            ans += bucket[freq]
            if len(ans) >= k:
                return ans[:k]


# 测试
if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))
    print(Solution().topKFrequent1(nums, k))
