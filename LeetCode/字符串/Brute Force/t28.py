class Solution:

    # BF算法 暴力匹配
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(haystack), len(needle)
        i, j = 0, 0
        while i < m and j < n:
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                i -= j - 1
                j = 0

        if j == n:
            return i - j
        else:
            return -1

if __name__ == '__main__':
    s = Solution()
    print(s.strStr("sadbutsad", "sad"))
    # print(s.strStr("leetcode", "leeto"))
