from typing import List

# 哈希表解法
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionarySet = set(dictionary)
        words = sentence.split(' ')
        for i, word in enumerate(words):
            for j in range(1, len(word) + 1):
                if word[:j] in dictionarySet:
                    words[i] = word[:j]
                    break
        return ' '.join(words)

# 测试
if __name__ == "__main__":
    dictionary = ["ax", "aaa", "aab", "aac", "aad"]
    sentence = "aaab"
    print(Solution().replaceWords(dictionary, sentence))
