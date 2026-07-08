from typing import List


class Solution:
    # 最简单最快的判断, set转换后是否长度有变化
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

    # 引入集合一个一个加
    def containsDuplicate1(self, nums: List[int]) -> bool:
        s = set()
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        return False

# 测试
if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    s = Solution()
    print(s.containsDuplicate(nums))
