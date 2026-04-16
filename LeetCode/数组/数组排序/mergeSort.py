class Solution:
    # 分解过程
    def mergeSort(self, arrs):
        if len(arrs) <= 1:
            return arrs

        mid = len(arrs) // 2
        left = self.mergeSort(arrs[:mid])
        right = self.mergeSort(arrs[mid:])

        return self.merge(left, right)

    # 合并过程
    def merge(self, left, right):
        res = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        if i < len(left):
            res.extend(left[i:])
        if j < len(right):
            res.extend(right[j:])
        return res


arr = [1, 9, 7, 5, 3, 6, 4]
s = Solution()
print(s.mergeSort(arr))