class MyCircularDeque:

    def __init__(self, k: int):
        self.capicity = k
        self.queue = [0] * k
        self.pront = 0
        self.rear = 0
        self.size = 0

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.pront = (self.pront - 1) % self.capicity
        self.queue[self.pront] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.capicity
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.pront = (self.pront + 1) % self.capicity
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.rear = (self.rear - 1) % self.capicity
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[self.pront]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1

        return self.queue[(self.rear - 1) % self.capicity]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capicity


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
