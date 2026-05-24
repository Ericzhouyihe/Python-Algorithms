class Queue:
    """
    顺序存储循环队列实现
    front 指向队头元素的前一个位置，rear 指向队尾元素所在位置
    """

    def __init__(self, size=100):
        """
        初始化空队列
        :param size: 队列最大容量（实际可用容量为 size）
        """
        self.size = size + 1  # 实际分配空间多一个，用于区分队满和队空
        self.queue = [None for _ in range(self.size)]  # 存储队列元素
        self.front = 0  # 队头指针，指向队头元素的前一个位置
        self.rear = 0  # 队尾指针，指向队尾元素所在位置

    def is_empty(self):
        """
        判断队列是否为空
        :return: True 表示队列为空，False 表示非空
        """
        return self.front == self.rear

    def is_full(self):
        """
        判断队列是否已满
        :return: True 表示队列已满，False 表示未满
        """
        return (self.rear + 1) % self.size == self.front

    def enqueue(self, value):
        """
        入队操作：在队尾插入元素
        :param value: 要插入的元素
        :raises Exception: 队列已满时抛出异常
        """
        if self.is_full():
            raise Exception("Queue is full")
        # rear 指针循环前进一位
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = value

    def dequeue(self):
        """
        出队操作：从队头删除元素并返回
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        # front 指针循环前进一位
        self.front = (self.front + 1) % self.size
        value = self.queue[self.front]
        self.queue[self.front] = None  # 可选：清除引用，便于垃圾回收
        return value

    def front_value(self):
        """
        获取队头元素
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[(self.front + 1) % self.size]

    def rear_value(self):
        """
        获取队尾元素
        :return: 队尾元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")
        return self.queue[self.rear]
