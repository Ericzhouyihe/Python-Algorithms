from typing import Counter, List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts = Counter(nums1)
        res = []

        for num in nums2:
            if counts.get(num, 0) > 0:
                res.append(num)
                counts[num] -= 1

        return res