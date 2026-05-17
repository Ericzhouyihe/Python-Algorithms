from typing import List

"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = 0
        stack = []

        heights = [0] + heights + [0]
        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                res = max(res, height * width)
            stack.append(i)

        return res


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.largestRectangleArea([2, 1, 5, 6, 2, 3]))
    print(s.largestRectangleArea([2, 4]))
    print(s.largestRectangleArea([1, 1]))
    print(s.largestRectangleArea([2, 1, 2]))
