class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        num = 1
        str = a
        if len(a) > len(b):
            if a.find(b) != -1:
                return num
            num += 1
            str = str + a
            return num if str.find(b) != -1 else -1

        if b.find(a) != -1:

            while str.find(b) == -1:
                num += 1
                str = str + a
            return num
        return -1


# 测试
if __name__ == '__main__':
    s = Solution()
    print(s.repeatedStringMatch('abcd', 'cdabcdab'))
    print(s.repeatedStringMatch('a', 'aa'))
    print(s.repeatedStringMatch("abc", "wxyz"))
