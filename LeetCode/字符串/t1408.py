from typing import List


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i, x in enumerate(words):
            for j, y in enumerate(words):
                if j != i and x in y:
                    ans.append(x)
                    break
        return ans