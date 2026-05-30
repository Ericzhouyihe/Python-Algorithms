import heapq


class PriorityQueue:
    def __init__(self):
        # 初始化一个空堆和自增索引
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        """
        入队操作，将元素 item 按照优先级 priority 压入堆中。
        为实现大顶堆，优先级取负数；index 保证相同优先级时的稳定性。
        """
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        """
        出队操作，弹出并返回优先级最高的元素（大顶堆）。
        """
        if not self.queue:
            raise IndexError("pop from empty priority queue")
        return heapq.heappop(self.queue)[-1]
