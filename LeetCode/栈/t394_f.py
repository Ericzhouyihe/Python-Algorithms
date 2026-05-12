class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        num = 0
        for c in s:
            if c == ']':
                temp = []
                while True:
                    n = stack.pop()
                    if n != '[':
                        temp.append(n)
                    else:
                        break
                for i in range(int(stack.pop())):
                    stack.append(''.join(temp)[::-1])
            else:
                if c.isdigit():
                    num = num * 10 + int(c)
                else:
                    if num != 0:
                        stack.append(num)
                        num = 0
                    stack.append(c)

        return ''.join(stack)


s = Solution()
print(s.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))
print(s.decodeString("2[abc]3[cd]ef"))
print(s.decodeString("100[leetcode]"))
print(s.decodeString("3[a2[c]]"))
