from typing import List


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        for s in queries:
            res.append(self.camel(s, pattern))
        return res

    def camel(self, query, pattern):
        n, m = len(query), len(pattern)
        if n < m:
            return False
        i = j = 0
        while i < n:
            if j < m and query[i] == pattern[j]:
                i += 1
                j += 1
            else:
                if ord(query[i]) < ord('a'):
                    return False
                i += 1
        return j == m
