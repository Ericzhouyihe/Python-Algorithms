# 数组实现节点
class Node:  # 字符节点
    def __init__(self):
        # 初始化字符节点
        # children 是长度为 26 的数组，分别对应 'a'~'z' 的子节点
        self.children = [None for _ in range(26)]  # 初始化所有子节点为 None
        self.isEnd = False  # isEnd 用于标记该节点是否为某个单词的结尾

# 哈希表实现节点
class Node:  # 字符节点
    def __init__(self):  # 初始化字符节点
        self.children = dict()  # 用哈希表存储所有子节点，key 为字符，value 为 Node 实例
        self.isEnd = False  # 标记该节点是否为某个单词的结尾
        # 例如：children['a'] 表示以当前节点为父节点，字符为 'a' 的子节点


class Trie:  # 字典树（前缀树）
    def __init__(self):
        """
        初始化字典树，创建一个根节点。
        根节点不存储任何字符，仅作为所有单词的公共起点。
        """
        self.root = Node()  # 初始化根节点（根节点不保存字符）

    # 向字典树中插入一个单词
    def insert(self, word: str) -> None:
        """
        将一个单词插入到字典树中。

        参数:
            word (str): 需要插入的单词
        """
        cur = self.root  # 从根节点开始
        for ch in word:  # 遍历单词中的每个字符
            # 如果当前节点的子节点中不存在字符 ch，则新建一个节点
            if ch not in cur.children:
                cur.children[ch] = Node()  # 创建新节点并加入子节点字典
            # 移动到下一个字符节点，继续插入
            cur = cur.children[ch]
        # 单词所有字符插入完成后，将当前节点标记为单词结尾
        cur.isEnd = True

        # 查找字典树中是否存在一个单词
        def search(self, word: str) -> bool:
            """
            在字典树中查找指定单词是否存在。

            参数:
                word (str): 需要查找的单词

            返回:
                bool: 如果单词存在于字典树中，返回 True；否则返回 False
            """
            cur = self.root  # 从根节点开始
            for ch in word:  # 遍历单词中的每个字符
                if ch not in cur.children:  # 如果当前节点的子节点中不存在该字符
                    return False  # 说明单词不存在，直接返回 False
                cur = cur.children[ch]  # 移动到对应的子节点，继续查找下一个字符
            return cur.isEnd  # 所有字符查找完毕，判断当前节点是否为单词结尾标记

        # 查找字典树中是否存在一个前缀
        def startsWith(self, prefix: str) -> bool:
            """
            在字典树中查找指定前缀是否存在。

            参数:
                prefix (str): 需要查找的前缀字符串

            返回:
                bool: 如果前缀存在于字典树中，返回 True；否则返回 False
            """
            cur = self.root  # 从根节点开始
            for ch in prefix:  # 遍历前缀中的每个字符
                if ch not in cur.children:  # 如果当前节点的子节点中不存在该字符
                    return False  # 说明前缀不存在，直接返回 False
                cur = cur.children[ch]  # 移动到对应的子节点，继续查找下一个字符
            return True  # 所有字符查找完毕，前缀存在于字典树中
