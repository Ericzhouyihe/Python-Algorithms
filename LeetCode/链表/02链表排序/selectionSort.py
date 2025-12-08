# 链表--选择排序
from LeetCode.链表.ListNode import ListNode


class Solution:
    def selectionSort(self, head: ListNode):
        node_index = head
        while node_index and node_index.next:
            # 假设当前节点为最小的节点
            min_node = node_index
            node_j = node_index.next

            while node_j:
                if node_j.val < min_node.val:
                    min_node = node_j
                node_j = node_j.next

            # 如果找到更小的值,则交换
            if node_index != min_node:
                node_index.val, min_node.val = min_node.val, node_index.val

            node_index = node_index.next

        return head
