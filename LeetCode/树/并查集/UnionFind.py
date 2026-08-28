class UnionFind:
    def __init__(self, n):
        """
        初始化并查集，将每个元素的集合编号初始化为其自身下标。
        :param n: 元素总数
        """
        self.ids = [i for i in range(n)]  # ids[i] 表示元素 i 所在集合的编号

    def find(self, x):
        """
        查找元素 x 所在集合的编号。
        :param x: 元素编号
        :return: x 所在集合的编号
        """
        return self.ids[x]

    def union(self, x, y):
        """
        合并包含元素 x 和 y 的两个集合。
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果 x 和 y 原本就在同一集合，返回 False；否则合并并返回 True
        """
        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            # x 和 y 已经在同一个集合，无需合并
            return False

        # 遍历所有元素，将属于 y_id 集合的元素编号改为 x_id，实现合并
        for i in range(len(self.ids)):
            if self.ids[i] == y_id:
                self.ids[i] = x_id
        return True

    def is_connected(self, x, y):
        """
        判断元素 x 和 y 是否属于同一个集合。
        :param x: 元素 x
        :param y: 元素 y
        :return: 如果属于同一集合返回 True，否则返回 False
        """
        return self.find(x) == self.find(y)
