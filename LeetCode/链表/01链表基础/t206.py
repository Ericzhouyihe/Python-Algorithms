from typing import Optional

from LeetCode.链表.LinkedList import create_linked_list, print_list
from LeetCode.链表.ListNode import  ListNode

class Solution:
    # 迭代法
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        return prev

    # 递归法
    def reverseList1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        newNode = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return newNode

# 测试用例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1：普通链表
    values1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(values1)
    print("原始链表：", end=" ")
    print_list(head1)
    reversed_head1 = solution.reverseList1(head1)
    print("结果链表：", end=" ")
    print_list(reversed_head1)