class Solution:
    # 不直接构建列表速度更快
    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        for i in range(len(lst)):
            lst[i] = lst[i][::-1]
        return " ".join(lst)

    def reverseWords(self, s: str) -> str:
        lst = s.split(" ")
        lst = [word[::-1] for word in lst]
        return " ".join(lst)
