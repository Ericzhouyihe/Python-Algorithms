class ArrayDeque:

    def __init__(self, capacity =100):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def is_empty(self):
        return self.size == self.capacity

    def push_front(self, value):
        if self.is_full():
            raise Exception("Deque is full")

        # 队头指针往前移动
        self.front = (self.front - 1) % self.capacity
        self.queue[self.front] = value
        self.size += 1

    def push_back(self, value):
        if self.is_full():
            raise Exception("Deque is full")

        self.queue[self.rear] = value
        # 队尾指针向后移动
        self.rear = (self.rear + 1) % self.capacity
        self.size += 1

    def pop_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        value = self.queue[self.front]
        # 队头指针往后移动
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return value

    def pop_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        # 队尾指针往前移动
        self.rear = (self.rear - 1) % self.capacity
        self.size -= 1

        return self.queue[self.rear]

    def peek_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        return self.queue[self.front]

    def peek_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        return self.queue[(self.rear - 1) % self.capacity]
