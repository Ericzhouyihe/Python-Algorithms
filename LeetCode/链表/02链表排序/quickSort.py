from LeetCode.链表.ListNode import ListNode


class Solution:
    def quickSort(self, left: ListNode, right: ListNode):
        """
        快速排序主函数
        :param left: 左边界节点(包含)
        :param right: 右边界节点(不包含)
        """
        if left == right or left.next == right:
            return left

        # 分割链表，获取基准值位置
        pi = self.partition(left, right)

        # 递归排序左右部分
        self.quickSort(left, pi)
        self.quickSort(pi.next, right)

        return left

    def partition(self, left: ListNode, right: ListNode):
        """
        分割函数-将链表分割成两部分
        :param left: 左边界节点(包含)
        :param right: 右边界节点(不包含)
        :return: 基准值节点的最终位置
        """
        if left == right or left.next == right:
            return left

        # 选择头节点为基准节点
        pivot = left.val

        # low_tail: 指向小于基准值的最后一个节点
        # node_i: 遍历指针，寻找小于基准值的节点
        low_tail, node_i = left, left.next

        while node_i != right:
            # 发现一个小于基准值的元素
            if node_i.val < pivot:
                # 将 low_tail 向右移动一位
                low_tail = low_tail.next
                # 交换 low_tail 和 node_i 的值，保证 low_tail 之前的节点都小于基准值
                low_tail.val, node_i.val = node_i.val, low_tail.val
            node_i = node_i.next

        # 将基准节点放到正确位置上（low_tail 位置）
        low_tail.val, left.val = left.val, low_tail.val
        return low_tail
