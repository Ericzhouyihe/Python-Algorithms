"""
基本计算器II
给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。
整数除法仅保留整数部分。
"""


class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        stack = []
        perSign = '+'
        num = 0
        for i in range(n):
            if s[i] != ' ' and s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
            if i == n - 1 or s[i] in '+-*/':
                if perSign == '+':
                    stack.append(num)
                elif perSign == '-':
                    stack.append(-num)
                elif perSign == '*':
                    stack.append(stack.pop() * num)
                else:
                    stack.append(int(stack.pop() / num))
                perSign = s[i]
                num = 0
        return sum(stack)
