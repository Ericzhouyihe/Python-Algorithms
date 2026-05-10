from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        dic = {}
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        for i in range(len(temperatures)):
            if i in dic:
                ans[i] = dic[i] - i
            else:
                ans[i] = 0
        return ans
