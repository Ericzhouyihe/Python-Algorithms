class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        visited = set()

        for i, ch in enumerate(s):
            if ch in visited:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                removed = stack.pop()
                visited.remove(removed)

            stack.append(ch)
            visited.add(ch)

        return "".join(stack)

    def removeDuplicateLetters1(self, s: str) -> str:
        """
        要让结果字典序最小，就希望前面的字符尽量小
        但又不能随便删，因为每个字母最后必须保留一次，而且不能打乱相对顺序
        所以当你遍历字符串时，遇到一个字符 c，如果栈顶字符比 c 大，并且栈顶字符后面还会再出现，那就可以把栈顶弹掉，让更小的 c 往前排
        判断“后面还会不会出现”，通常用每个字符最后一次出现的位置
        """

        last = {ch: i for i, ch in enumerate(s)}
        stack = []
        used = set()

        for i, ch in enumerate(s):
            if ch in used:
                continue

            while stack and stack[-1] > ch and last[stack[-1]] > i:
                used.remove(stack.pop())

            stack.append(ch)
            used.add(ch)

        return "".join(stack)


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.removeDuplicateLetters1("bcabc"))
    print(s.removeDuplicateLetters1("cbacdcbc"))
