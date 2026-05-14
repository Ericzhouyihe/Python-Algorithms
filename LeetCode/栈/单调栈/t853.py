from typing import List


class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        slowest_time = 0

        for p, s in cars:
            time = (target - p) / s

            if time > slowest_time:
                fleets += 1
                slowest_time = time

        return fleets
