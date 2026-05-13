from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ret = [-1] * n
        stk = list()

        for i in range(n * 2 - 1):
            while stk and nums[stk[-1]] < nums[i % n]:
                ret[stk.pop()] = nums[i % n]
            stk.append(i % n)

        return ret


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElements([1, 2, 1]))
    print(s.nextGreaterElements([1, 2, 3, 4, 3]))
    print(s.nextGreaterElements([5, 4, 3, 2, 1]))
    print(s.nextGreaterElements([2, 4]))
    print(s.nextGreaterElements([1, 2, 3, 4, 3, 5]))
