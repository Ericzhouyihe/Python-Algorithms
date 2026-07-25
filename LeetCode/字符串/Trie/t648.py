from typing import List

class trie:
    def __init__(self):
        self.children = {}
        self.value = None

    def add(self, str):
        node = self
        for ch in str:
            if ch not in node.children:
                node.children[ch] = trie()
            node = node.children[ch]
        node.value = str

    def search(self, str):
        node = self
        for ch in str:
            if ch not in node.children:
                return None
            if node.value is not None:
                return node.value
            node = node.children[ch]

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        tree = trie()
        for dic in dictionary:
            tree.add(dic)
        strs = sentence.split(" ")
        for i in range(len(strs)):
            str = tree.search(strs[i])
            if str:
                strs[i] = str 
        return " ".join(strs)

# 测试
if __name__ == '__main__':
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(Solution().replaceWords(dictionary, sentence))
