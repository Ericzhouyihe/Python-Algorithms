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
