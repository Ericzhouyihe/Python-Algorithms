class WordDictionary:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def addWord(self, word: str) -> None:
        node = self
        for ch in word:
            if ch not in node.children:
                node.children[ch] = WordDictionary()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        # 内部递归
        def dfs(index: int, node) -> bool:
            if index == len(word):
                return node.isEnd

            ch = word[index]

            if ch == '.':
                # 通配符：所有子节点都试一遍
                for child in node.children.values():
                    if dfs(index + 1, child):
                        return True
                return False
            else:
                # 普通字符
                if ch not in node.children:
                    return False
                return dfs(index + 1, node.children[ch])

        return dfs(0, self)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)