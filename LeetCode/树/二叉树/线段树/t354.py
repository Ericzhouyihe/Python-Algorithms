from typing import List


# 动态规划题
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0
        size = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        dp = [1 for _ in range(size)]

        for i in range(size):
            for j in range(i):
                if envelopes[j][1] < envelopes[i][1]:
                    dp[i] = max(dp[i], dp[i] + 1)

        return max(dp)
