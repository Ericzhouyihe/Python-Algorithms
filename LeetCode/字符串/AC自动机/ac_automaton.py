class TrieNode:
    def __init__(self):
        self.children = {}  # 子节点，key 为字符，value 为 TrieNode
        self.fail = None  # 失配指针，指向当前节点最长可用后缀的节点
        self.is_end = False  # 是否为某个模式串的结尾
        self.word = ""  # 如果是结尾，存储完整的单词

class AC_Automaton:
    def __init__(self):
        self.root = TrieNode()  # 初始化根节点

    def add_word(self, word):
        """
        向Trie树中插入一个模式串
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()  # 新建子节点
            node = node.children[char]
        node.is_end = True  # 标记单词结尾
        node.word = word  # 存储完整单词

    def build_fail_pointers(self):
        """
        构建失配指针（fail指针），采用BFS广度优先遍历
        """
        from collections import deque

        queue = deque()
        # 1. 根节点的所有子节点的 fail 指针都指向根节点
        for child in self.root.children.values():
            child.fail = self.root
            queue.append(child)

        # 2. 广度优先遍历，依次为每个节点建立 fail 指针
        while queue:
            current = queue.popleft()
            for char, child in current.children.items():
                # 从当前节点的 fail 指针开始，向上寻找有无相同字符的子节点
                fail = current.fail
                while fail and char not in fail.children:
                    fail = fail.fail
                # 如果找到了，child的fail指针指向该节点，否则指向根节点
                child.fail = (
                    fail.children[char] if fail and char in fail.children else self.root
                )
                queue.append(child)

    def search(self, text):
        """
        在文本text中查找所有模式串出现的位置
        返回所有匹配到的模式串（可重复）
        """
        result = []
        node = self.root

        for char in text:
            # 如果当前节点没有该字符的子节点，则沿fail指针向上跳转
            while node is not self.root and char not in node.children:
                node = node.fail
            # 如果有该字符的子节点，则转移到该子节点
            if char in node.children:
                node = node.children[char]
            # 否则仍然停留在根节点

            # 检查当前节点以及沿fail链上的所有节点是否为单词结尾
            temp = node
            while temp is not self.root:
                if temp.is_end:
                    result.append(temp.word)  # 记录匹配到的模式串
                temp = temp.fail

        return result