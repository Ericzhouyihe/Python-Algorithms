from typing import List

class Solution:
    # 集合
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        
        for i in range(len(nums)):
            if nums[i] in nums[i+1:i+k+1]:
                return True
        
        return False


    # 使用字典, 值对应索引值
    def containsNearbyDuplicate1(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return False
        d = {}
        for i in range(len(nums)):
            if nums[i] in d and i - d[nums[i]] <= k:
                return True
            d[nums[i]] = i
        return False


# 测试
if __name__ == '__main__':
    nums = [1, 2, 3, 1]
    k = 3
    s = Solution()
    print(s.containsNearbyDuplicate(nums, k))
