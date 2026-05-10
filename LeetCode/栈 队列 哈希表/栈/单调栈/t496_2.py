# 单调栈 + 哈希表
from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        stack = []
        dic = {}
        for i in range(len(nums2)):
            # stack不为空，且栈顶元素小于当前元素，则栈顶索引出栈
            while stack and nums2[stack[-1]] < nums2[i]:
                # 出栈的元素记录一个他右方的第一个最大值
                dic[nums2[stack.pop()]] = nums2[i]
            # 直到栈顶元素比当前元素大，或栈为空时，直接存入当前元素的索引
            stack.append(i)
        for i in nums1:
            if i in dic:
                res.append(dic[i])
            else:
                res.append(-1)
        return res


# 测试
if __name__ == "__main__":
    s = [1, 2, 3, 4, 5]
    print(s.index(2))
    print(s[2])
    s = Solution()
    print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))
