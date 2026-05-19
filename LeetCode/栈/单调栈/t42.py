from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        每个位置 i 能接多少水，取决于它左边最高柱子和右边最高柱子中较矮的那个
        水会从矮的一侧流走,所以只能由两边较矮的挡板决定
        """
        n = len(height)
        if n == 0:
            return 0

        # 初始化左最大和右最大数组
        leftMax = [0] * n
        rigthMax = [0] * n

        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])

        rigthMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rigthMax[i] = max(rigthMax[i + 1], height[i])

        ans = 0
        for i in range(n):
            ans += min(leftMax[i], rigthMax[i]) - height[i]

        return ans

    def trap1(self, height: List[int]) -> int:
        """
        通过双指针进行优化, 同时维护左边最高和右边最高
        对于某个位置i, 他能接的水是 min(左边最高,右边最高)-当前高度
        所以外层先判断了,左边和右边比较小的值
        内层进行更新当前的最高值, 或计算当前位置的蓄水量
        """
        left, right = 0, len(height) - 1
        leftMax = rightMax = 0
        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= leftMax:
                    leftMax = height[left]
                else:
                    ans += leftMax - height[left]
                left += 1
            else:
                if height[right] >= rightMax:
                    rightMax = height[right]
                else:
                    ans += rightMax - height[right]
                right -= 1

        return ans


# 测试
if __name__ == "__main__":
    s = Solution()
    print(s.trap1([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(s.trap1([4, 2, 0, 3, 2, 5]))
