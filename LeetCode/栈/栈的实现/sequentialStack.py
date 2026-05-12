# 顺序栈的实现
class sequentialStack:
    def __init__(self, size=100):
        self.stack = []
        self.size = size
        self.top = -1  # 栈顶指针，-1表示空栈

    def is_empty(self):
        # 判断栈是否为空
        return self.top == -1

    def is_full(self):
        # 判断栈是否是满的
        return self.top + 1 == self.size

    def push(self, value):
        # 入栈操作
        if self.is_full():
            raise Exception('栈已满')
        self.stack.append(value)
        self.top += 1

    def pop(self):
        # 出栈操作
        if self.is_empty():
            raise Exception('栈为空')
        self.top -= 1
        return self.stack.pop()

    def peek(self):
        # 查看栈顶元素
        if self.is_empty():
            raise Exception('栈为空')
        return self.stack[self.top]