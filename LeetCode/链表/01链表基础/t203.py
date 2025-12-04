from typing import Optional

from LeetCode.链表.ListNode import print_list, create_linked_list, ListNode


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = new_list_node = ListNode(next=head)
        while curr.next:
            if curr.next.val == val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return new_list_node.next


# 测试用例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1：普通链表
    values1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(values1)
    print("原始链表：", end=" ")
    print_list(head1)
    reversed_head1 = solution.removeElements(head1, 2)
    print("结果链表：", end=" ")
    print_list(reversed_head1)
