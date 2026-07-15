class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        lst = list(s)
        for i in range(n):
            temp = lst[0]
            lst.pop(0)
            lst.append(temp)
            if ''.join(lst) == goal:
                return True
        return False
