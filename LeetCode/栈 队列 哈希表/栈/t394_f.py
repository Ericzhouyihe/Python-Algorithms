class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c == ']':
                temp = []
                while True:
                    n = stack.pop()
                    if n != '[':
                        temp.append(n)
                    else:
                        break
                num = int(stack.pop())
                for i in range(num):
                    for j in range(len(temp)-1, -1, -1):
                        stack.append(temp[j])
            else:
                stack.append(c)
        return ''.join(stack)


s = Solution()
print(s.decodeString("100[leetcode]"))