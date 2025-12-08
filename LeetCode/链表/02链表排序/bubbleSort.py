# 冒泡排序
from LeetCode.链表.ListNode import ListNode


class Solution:
    def bubbleSort(self, head: ListNode):
        if not head or not head.next:
            return head

        # 外层循环:控制排序轮数
        sort_round = head
        # 尾指针,右侧为已排序部分
        tail = None

        while sort_round:
            node_i = head  # 内层循环指针

            # 内层循环:比较相邻的节点
            while node_i and node_i.next != tail:
                if node_i.val > node_i.next.val:
                    # 交换相邻节点的值
                    node_i.val, node_i.next.val = node_i.next.val, node_i.val
                node_i = node_i.next

            # 更新尾指针
            tail = node_i
            sort_round = sort_round.next

        return head
