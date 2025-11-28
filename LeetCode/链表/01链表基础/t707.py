class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index: int) -> int:
        if index < 0 or index > self.size:
            return -1
        curr = self.head
        for i in range(index + 1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        curr = self.head
        for i in range(index):
            curr = curr.next
        add_node = ListNode(val)
        add_node.next = curr.next
        curr.next = add_node

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        curr = self.head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
