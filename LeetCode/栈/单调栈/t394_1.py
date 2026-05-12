class Solution:
    # 递归

    def decodeString(self, s: str) -> str:
        pass


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))  # "aaabcbc"
    print(s.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(s.decodeString("3[a2[c]]"))  # "accaccacc"
