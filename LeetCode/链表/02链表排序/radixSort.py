from LeetCode.链表.ListNode import ListNode


class Solution:
    def radixSort(self, head: ListNode):
        # 1,计算最大数字的位数
        size = 0
        cur = head
        while cur:
            val_len = len(str(cur.val))
            size = max(size, val_len)
            cur = cur.next

        # 2,从个位到最高位依次排序
        for i in range(size):
            # 创建10个桶(对应数字 0-9)
            buckets = [[] for _ in range(10)]
            cur = head

            # 3,按当前位数字分配到对应的桶
            while cur:
                # 获取第 i 位数字：先除以 10^i，再对 10 取余
                digit = (cur.val // (10 ** i)) % 10
                buckets[digit].append(cur.val)

            dummy_head = ListNode(-1)
            cur = dummy_head
            for bucket in buckets:
                for num in bucket:
                    cur.next = ListNode(num)
                    cur = cur.next

            head = dummy_head.next

        return head
