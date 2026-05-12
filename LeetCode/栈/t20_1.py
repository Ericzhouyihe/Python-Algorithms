# 有效的括号
"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。
有效字符串需满足：
左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
每个右括号都有一个对应的相同类型的左括号。
"""
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False

        # 初始化字典，键为右括号，值为左括号
        pairs = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        # 定义一个集合
        stack = []
        # 遍历字符串
        for ch in s:
            # 判断当前字符是否为字典中的键（也就是判断当前字符是否为右括号）
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
                print(stack)

        return not stack