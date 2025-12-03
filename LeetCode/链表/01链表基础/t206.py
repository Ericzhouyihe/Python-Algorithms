from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


# for test
# 辅助函数：打印链表
def print_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# 辅助函数：创建链表
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

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