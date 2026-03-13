# 顺序栈的实现
class sequentialStack:
    def __init__(self, size=100):
        self.stack = []
        self.size = size
        self.top = -1  # 栈顶指针，-1表示空栈

    def is_empty(self):
        return self.top == -1
