class Solution:
    def calculate(self, s: str) -> int:
        lst = []
        preSign = '+'
        res = 0
        for i, ch in enumerate(s):
            if ch != ' ' and ch.isdigit():
                res = res * 10 + ord(ch) - ord('0')
            if ch in "+-*/" or i == len(s) - 1:
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