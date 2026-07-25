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
            node = node.children[ch]
            if node.value:
                return node.value

# 字典树解法
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

# 优化
class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for w in word + "#":
            if w not in node:
                node[w] = {}
            node = node[w]

    def find(self, word: str) -> str:
        node = self.root
        for i in range(len(word)):
            if "#" in node:
                return word[:i]
            if word[i] in node:
                node = node[word[i]]
            else:
                break
        return word

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        for d in dictionary:
            trie.insert(d)
        words = sentence.split(" ")
        return " ".join(trie.find(word) for word in words)

# 测试
if __name__ == '__main__':
    dictionary = ["ax", "aaa", "aab", "aac", "aad"]
    sentence = "aaab"
    print(Solution().replaceWords(dictionary, sentence))
