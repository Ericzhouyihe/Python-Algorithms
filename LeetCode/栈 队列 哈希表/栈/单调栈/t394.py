class Solution:
    # 辅助栈

    def decodeString(self, s: str) -> str:
        stack, res, multi = [], "", 0
        for c in s:
            if c == "[":
                stack.append([multi, res])
                res, multi = "", 0
            elif c == "]":
                cur_multi, last_res = stack.pop()
                res = last_res + cur_multi * res
            elif c.isdigit():
                multi = 10 * multi + int(c)
            else:
                res += c
        return res


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.decodeString("3[a]2[bc]"))  # "aaabcbc"
    print(s.decodeString("2[abc]3[cd]ef"))  # "abcabccdcdcdef"
    print(s.decodeString("3[a2[c]]"))  # "accaccacc"
