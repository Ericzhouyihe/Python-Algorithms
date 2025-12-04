from typing import Optional

from LeetCode.链表.ListNode import print_list, create_linked_list, ListNode


class Solution:
    def oddEvenList(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head:
            return None

        return head


# 测试用例
if __name__ == "__main__":
    solution = Solution()

    # 测试用例1：普通链表
    values1 = [1, 2, 3, 4, 5]
    head1 = create_linked_list(values1)
    print("原始链表：", end=" ")
    print_list(head1)
    reversed_head1 = solution.oddEvenList(head1)
    print("结果链表：", end=" ")
    print_list(reversed_head1)