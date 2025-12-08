from typing import Optional

from LeetCode.链表.ListNode import ListNode


class LinkedList:
    def __init__(self):
        self.head = None  # 链表头指针，初始为 None


# 辅助函数：打印链表
def print_list(head: Optional[ListNode]):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# 根据 data 列表初始化一个新链表
def create_linked_list(self, data):
    if not data:
        # 如果输入数据为空，直接返回，不创建链表
        return
    # 创建头节点，并将 head 指向头节点
    self.head = ListNode(data[0])
    cur = self.head  # cur 用于指向当前链表的尾节点
    # 依次遍历 data 中剩余的元素，逐个创建新节点并连接到链表尾部
    for i in range(1, len(data)):
        node = ListNode(data[i])  # 创建新节点
        cur.next = node  # 将新节点连接到当前尾节点
        cur = cur.next  # cur 指向新的尾节点，准备连接下一个节点


# 获取线性链表长度
def length_linked_list(self):
    count = 0  # 初始化计数器，记录节点个数
    cur = self.head  # 从链表头节点开始遍历
    while cur:  # 只要当前节点不为 None，就继续遍历
        count += 1  # 每遍历到一个节点，计数器加 1
        cur = cur.next  # 指针后移，指向下一个节点
    return count  # 返回计数器的值，即链表长度


# 链表中查找值为 val 的节点
def find_node(self, val):
    cur = self.head  # 从链表头节点开始遍历
    while cur:  # 只要当前节点不为 None，就继续遍历
        if val == cur.val:  # 如果当前节点的值等于目标值，查找成功
            return cur  # 返回当前节点
        cur = cur.next  # 指针后移，指向下一个节点

    # 遍历完整个链表都没有找到目标值，返回 None
    return None


# 插入节点
def insert_node(self, index, val):
    # 头部插入（index == 1）
    if index == 1:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        return None

    count = 0
    cur = self.head
    # 遍历链表，找到第 index - 1 个节点（即新节点的前驱节点）
    while cur and count < index - 1:
        cur = cur.next
        count += 1

    # 如果遍历到链表末尾还没找到前驱节点，说明 index 越界，插入失败
    if not cur:
        return 'Error'

    node = ListNode(val)
    # 尾部插入（index 指向最后一个节点的下一个位置）
    if cur.next is not None:
        node.next = cur.next

    cur.next = node


# 改变元素：将链表中第 i 个元素值改为 val
def change(self, index, val):
    # 初始化计数器 count 和指针 cur，cur 指向链表头节点
    count = 0
    cur = self.head
    # 遍历链表，直到找到第 index 个节点
    while cur and count < index:
        count += 1
        cur = cur.next

    # 如果 cur 为空，说明 index 越界，返回错误
    if not cur:
        return 'Error'

    # 修改第 index 个节点的值为 val
    cur.val = val

# 链表删除元素
def removeInside(self, index):
    # 初始化计数器 count 和指针 cur，cur 指向链表头节点
    count = 0
    cur = self.head

    # 遍历链表，cur 移动到第 index - 1 个节点（即待删除节点的前驱）
    while cur.next and count < index - 1:
        count += 1
        cur = cur.next

    # 如果 cur 为空，说明 index 越界，返回错误
    if not cur:
        return 'Error'

    # del_node 指向待删除的节点
    del_node = cur.next
    # 将 cur 的 next 指针指向 del_node 的下一个节点，实现删除
    cur.next = del_node.next