class Solution:
    def calculate(self, s: str) -> int:
        lst = []
        preSign = '+'
        res = 0
        for ch in s:
            if ch != ' ' and ch.isdigit():
                res = res * 10 + ord(ch) - ord('0')
            # 这里使用 ch == s[-1] 不能正确的判断出该字符是字符串的最后一个字符，想判断是最后一个，只能用索引进行判断
            if ch in "+-*/" or ch == s[-1]:
                if preSign == '+':
                    lst.append(res)
                elif preSign == '-':
                    lst.append(-res)
                elif preSign == '*':
                    lst.append(lst.pop() * res)
                else:
                    lst.append(int(lst.pop() / res))
                preSign = ch
                res = 0
        return sum(lst)

s = Solution()
s.calculate("3+2*2")