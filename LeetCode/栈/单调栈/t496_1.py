# 暴力法
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        res = [0] * m
        for i in range(m):
            j = nums2.index(nums1[i])
            k = j + 1
            # 比nums2[j]下，就跳过，直到找到比nums2[j]大的，或者k越界了
            while k < n and nums2[k] < nums2[j]:
                k += 1
            res[i] = nums2[k] if k < n else -1
        return res
