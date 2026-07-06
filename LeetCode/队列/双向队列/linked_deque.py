class Node:
    # 双向链表节点
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class linkedDoubleQueue:
    def __init__(self):
        # 头节点
        self.head = Node(0)
        # 尾节点
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
        # 队列大小
        self.size = 0       

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    # 队头入队
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        self.head.next.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node
        self.size += 1

    # 队尾入队
    def push_back(self, value):
        new_node = Node(value)
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail.prev
        self.size += 1

    # 对头出队
    def pop_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        pop_node = self.head.next
        self.head.next = pop_node.next
        pop_node.next.prev = self.head
        self.size -= 1
        return pop_node.value

    # 对尾出队
    def pop_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")

        pop_node = self.tail.prev
        self.tail.prev = pop_node.prev
        pop_node.prev.next = self.tail.prev
        self.size -= 1
        return pop_node.value

    # 查看第一个元素
    def peek_front(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.head.next.value

    # 查看最后一个元素
    def peek_back(self):
        if self.is_empty():
            raise Exception("Deque is empty")
        return self.tail.prev.value
