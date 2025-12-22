from typing import Optional
from LeetCode.链表.ListNode import ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return None

        slow, fast = head, head

        while True:
            if not fast or not fast.next:
                return None
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break

        res = head
        while res != slow:
            res, slow = res.next, slow.next

        return res
