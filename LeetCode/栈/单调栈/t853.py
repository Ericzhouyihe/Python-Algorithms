from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        贪心 直接计数
        先按 position 从大到小排序，也就是从最靠近终点的车开始看。
        因为前面的车不会被后面的车影响，后面的车只能追前面的车。
        对于每辆车，计算它单独到终点的时间：
        如果当前车到达时间 <= 前面车队到达时间
        说明它能追上前面的车队，加入同一个车队。
        如果当前车到达时间 > 前面车队到达时间
        说明它太慢，追不上前面的车队，只能自己形成新车队。
        """

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0

        for p, s in cars:
            time = (target - p) / s

            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets

    def carFleet1(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        单调栈思路:
        先排序好,
        """
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for p, s in cars:
            time = (target - p) / s

            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)


# 测试
if __name__ == "__main__":
    target = 12
    position = [10, 8, 0, 5, 3]
    speed = [2, 4, 1, 1, 3]
    s = Solution()
    print(s.carFleet(target, position, speed))
    print(s.carFleet1(target, position, speed))
