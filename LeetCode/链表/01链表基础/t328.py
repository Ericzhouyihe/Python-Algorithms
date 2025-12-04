from typing import Optional

from LeetCode.链表.ListNode import print_list, create_linked_list, ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        two = head.next
        odd = head
        even = two
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        odd.next = two
        return head


# 测试用例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1：普通链表
    values = [1, 2, 3, 4, 5]
    head = create_linked_list(values)
    print("原始链表：", end=" ")
    print_list(head)
    reversed_head1 = solution.oddEvenList(head)
    print("结果链表：", end=" ")
    print_list(reversed_head1)