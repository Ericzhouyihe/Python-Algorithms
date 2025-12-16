from LeetCode.链表.ListNode import ListNode


class Solution:
    def bucketSort(self, head, bucket_size=5):
        """
        链表桶排序
        :param head: 待排序的链表头节点
        :param bucket_size: 每个桶的大小，默认5
        :return: 排序后的链表头节点
        """
        if not head:
            return head

        # 计算链表里的最小值和最大值
        list_min, list_max = head.val, head.val
        cur = head
        while cur:
            if cur.val < list_min:
                list_min = cur.val
            if cur.val > list_max:
                list_max = cur.val
            cur = cur.next

        # 计算桶的数量并初始化桶
        bucket_count = (list_max - list_min) // bucket_size + 1
        buckets = [None for i in range(bucket_count)]

        # 讲链表元素分配到对应的桶中
        cur = head
        while cur:
            # 计算元素应该放入哪个桶中,并将节点插入其中
            index = (cur.val - list_min) // bucket_size
            self.insertion(buckets, index, cur.val)
            cur = cur.next

        # 对每个桶里的节点进行排序,然后合并
        dummy_head = ListNode(-1)
        cur = dummy_head

        for bucket_head in buckets:
            if bucket_head:
                # 对桶内元素机型归并排序
                sorted_bucket = self.mergeSort(bucket_head)
                # 将排序后的桶内元素添加到结果链表
                while sorted_bucket:
                    cur.next = sorted_bucket
                    cur = cur.next
                    sorted_bucket = sorted_bucket.next

        return dummy_head.next


    def insertion(self, buckets, index, val):
        """
        将节点插入桶中(头插法)
        :param buckets: 桶数组
        :param index: 桶的索引
        :param val: 要插入的值
        """
        if not buckets[index]:
            # 如果桶为空,直接创建节点
            buckets[index] = ListNode(val)
            return

        # 头插法:新节点插入到桶的头部
        node = ListNode(val)
        node.next = buckets[index]
        buckets[index] = None

    def mergeSort(self, head):
        """
        对链表进行归并排序
        :param head: 链表头节点
        :return: 排序后的链表头节点
        """
        if not head or not head.next:
            return head

        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        left_head, right_head = head, slow.next
        slow.next = None

        return self.merge(self.mergeSort(left_head), self.mergeSort(right_head))

    def merge(self, left, right):
        """
        归并两个有序链表
        :param left: 左链表头节点
        :param right: 右链表头节点 
        :return: 合并后的有序链表头节点
        """
        dummy_head = ListNode(-1)
        cur = dummy_head

        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next

        if left:
            cur.next = left
        if right:
            cur.next = right

        return dummy_head.next
