class Node:
    """
    链表节点类
    """

    def __init__(self, value):
        self.value = value  # 节点存储的值
        self.next = None  # 指向下一个节点的指针


class Queue:
    """
    链式队列实现
    """

    def __init__(self):
        """
        初始化空队列，创建一个头结点（哨兵节点），front和rear都指向头结点
        """
        head = Node(0)  # 哨兵节点，不存储有效数据
        self.front = head  # front指向队头元素的前一个节点
        self.rear = head  # rear指向队尾节点

    def is_empty(self):
        """
        判断队列是否为空
        :return: 如果队列为空返回 True，否则返回 False
        """
        return self.front == self.rear

    def enqueue(self, value):
        """
        入队操作，在队尾插入新节点
        :param value: 要插入的元素值
        """
        node = Node(value)  # 创建新节点
        self.rear.next = node  # 当前队尾节点的next指向新节点
        self.rear = node  # rear指针后移，指向新节点

    def dequeue(self):
        """
        出队操作，删除队头元素
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        node = self.front.next  # 队头节点（第一个有效节点）
        self.front.next = node.next  # front的next指向下一个节点
        if self.rear == node:  # 如果出队后队列为空，rear回退到front
            self.rear = self.front
        value = node.value  # 取出队头元素的值
        del node  # 释放节点（可省略，Python自动垃圾回收）
        return value

    def front_value(self):
        """
        获取队头元素的值
        :return: 队头元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.front.next.value  # front.next为队头节点

    def rear_value(self):
        """
        获取队尾元素的值
        :return: 队尾元素的值
        :raises Exception: 队列为空时抛出异常
        """
        if self.is_empty():
            raise Exception("Queue is empty")

        return self.rear.value  # rear为队尾节点
