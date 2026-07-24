from typing import List


class Trie:

    def __init__(self):
        self.children = {}
        self.isEnd = False

    def insert(self, word: str) -> None:
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = Trie()
            cur = cur.children[ch]
        cur.isEnd = True

    def search(self, word: str) -> bool:
        cur = self
        for ch in word:
            if ch in cur.children: 
                cur = cur.children[ch]
            else:
                if ord(ch) < 96:
                    return False
        
        return cur is not None and cur.isEnd


class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        trie_tree = Trie()
        trie_tree.insert(pattern)
        res = []
        for query in queries:
            res.append(trie_tree.search(query))
        return res
