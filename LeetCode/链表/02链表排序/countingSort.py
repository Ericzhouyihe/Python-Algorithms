from LeetCode.链表.ListNode import ListNode


class Solution:
    # 计数排序
    def countingSort(self, head: ListNode):
        if not head or not head.next:
            return head

        list_min, list_max = head.val, head.val
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next

        size = list_max - list_min + 1

        counts = [0 for i in range(size)]
        cur = head
        while cur:
            # 将数值映射到计数数组的索引
            index = cur.val - list_min
            counts[index] += 1
            cur = cur.next

        dummy_head = ListNode(-1)
        cur = dummy_head

        for i in range(size):
            while counts[i] > 0:
                new_node = ListNode(i + list_min)
                cur.next = new_node
                cur = cur.next
                counts[i] -= 1
        return dummy_head.next
