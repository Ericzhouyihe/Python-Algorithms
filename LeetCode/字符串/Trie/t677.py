# Python原生数据结构实现
class MapSum:
    def __init__(self):
        self.map = {}

    def insert(self, key: str, val: int) -> None:
        self.map[key] = val

    def sum(self, prefix: str) -> int:
        res = 0
        for key,val in self.map.items():
            if key.startswith(prefix):
                res += val
        return res

# 字典树trie 太慢了, 还没使用原生现有的快
class MapSum:
    def __init__(self):
        self.children = {}
        self.value = None

    def insert(self, key: str, val: int) -> None:
        node = self
        for ch in key:
            if ch not in node.children:
                node.children[ch] = MapSum()
            node = node.children[ch]
        self.value = val

    def sum(self, prefix: str) -> int:
        node = self
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children
        return self.dfs(node)

    def dfs(self, node):
        if not node:
            return 0
        res = node.value
        for node in node.children.values():
            res += self.dfs(node)
        return res
