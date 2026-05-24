class Queue:
    """
    顺序存储队列实现（非循环队列）
    front 指向队头元素的前一个位置，rear 指向队尾元素所在位置
    """

    def __init__(self, size=100):
        """
        初始化空队列
        :param size: 队列最大容量
        """
        self.size = size
        self.queue = [None for _ in range(size)]  # 存储队列元素的数组
        self.front = -1  # 队头指针，指向队头元素的前一个位置
        self.rear = -1  # 队尾指针，指向队尾元素所在位置

    def is_empty(self):
        """
        判断队列是否为空
        :return: 如果队列为空返回 True，否则返回 False
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return: 如果队列已满返回 True，否则返回 False
        """
        return self.rear + 1 == self.size

    def enqueue(self, value):
        """
        入队操作：在队尾插入元素
        :param value: 待插入的元素
        :raises Exception: 队列已满时抛出异常
        """
        if self.is_full():
            raise Exception("Queue is full")
        self.rear += 1
        self.queue[self.rear] = value

    def dequeue(self):
        """
        出队操作：从队头删除元素并返回
        :return: 队头元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        self.front += 1
        return self.queue[self.front]

    def front_value(self):
        """
        获取队头元素（不删除）
        :return: 队头元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.front + 1]

    def rear_value(self):
        """
        获取队尾元素（不删除）
        :return: 队尾元素
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.rear]
