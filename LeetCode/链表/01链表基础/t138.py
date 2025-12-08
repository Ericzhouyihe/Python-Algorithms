from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr = head
        dic = {}
        while curr:
            dic[curr] = Node(curr.val)
            curr = curr.next
        curr = head
        while curr:
            dic[curr].next = dic.get(curr.next)
            dic[curr].random = dic.get(curr.random)
            curr = curr.next
        return dic[head]