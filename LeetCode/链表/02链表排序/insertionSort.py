from LeetCode.链表.ListNode import ListNode


# 快慢指针法找到中间节点
def findMid(head):
    slow = head
    fast = head.next
    while not fast and not fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# 合并两个有序链表
def mergeLists(l1, l2):
    prev = ListNode(-1)
    curr = prev
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    if l1:
        curr.next = l1
    if l2:
        curr.next = l2

    return prev.next


class Solution:
    # 递归法
    def insertionSortList(self, head: ListNode):
        # 递归结束的条件
        if not head or not head.next:
            return head

        # 找到链表的中间节点
        mid = findMid(head)
        right_head = mid.next
        mid.next = None

        left = self.insertionSortList(head)
        right = self.insertionSortList(right_head)

        return mergeLists(left, right)

    # 哑节点法暴力解答
    def insertionSort(self, head: ListNode):
        if not head or not head.next:
            return head

        # 创建哑节点,简化边界情况处理
        dummy_head = ListNode(-1)
        dummy_head.next = head

        # 已经排序部分的尾节点
        sorted_tail = head
        # 当前插入的节点
        cur = head.next

        while cur:
            if sorted_tail.val <= cur.val:
                # sorted_tail已经在正确的位置
                sorted_tail = sorted_tail.next
            else:
                # 需要插入cur到已排序部分的合适位置
                prev = dummy_head
                # 找到插入位置：第一个大于 cur.val 的节点的前一个位置
                while prev.next.val <= cur.val:
                    prev = prev.next

                # 执行插入操作
                sorted_tail.next = cur.next  # 从原位置移除cur
                cur.next = prev.next  # cur指向下一个节点
                prev.next = cur  # 前一个节点指向cur

            cur = sorted_tail.next

        return dummy_head.next
