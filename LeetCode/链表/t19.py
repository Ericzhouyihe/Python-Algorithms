from typing import Optional

from LeetCode.链表.ListNode import ListNode


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = ListNode(-1)
        pre.next = head
        slow, fast = pre, pre
        for i in range(n):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return pre.next
