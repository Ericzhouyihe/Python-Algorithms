from LeetCode.链表.ListNode import ListNode


class Solution:
    def mergeSort(self, head: ListNode):
        # 分割阶段
        if not head or not head.next:
            return head

        # 快慢指针找到中间节点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        #  断开左右子链表
        left_head, right_head = head, slow.next
        slow.next = None

        # 归并操作
        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))

    def merge(self, head1, head2):
        # 归并阶段
        dummy_head = ListNode(-1)
        cur = dummy_head
        while left and right:
            if left.val <= right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        elif right:
            cur.next = right

        return dummy_head.next
