import heapq

class Solution:
    # 暴力法：统计每个字符个数之后进行排序
    def frequencySort(self, s: str) -> str:
        frequency = {}
        for i in s:
            frequency[i] = frequency.setdefault(i, 0) + 1
        lst = list(frequency.items())
        lst.sort(key=lambda x:x[1],reverse=True)
        result = "".join(c * n for c, n in lst)
        return result

    # 优先队列
    def frequencySort1(self, s: str) -> str:
        # 统计元素频数
        s_dict = {}
        for i in s:
            s_dict[i] = s_dict.setdefault(i, 0) + 1

        priority_queue = []
        for ch in s_dict:
            heapq.heappush(priority_queue, (-s_dict[ch], ch))

        res = []
        while priority_queue:
            ch = heapq.heappop(priority_queue)[-1]
            times = s_dict[ch]
            while times:
                res.append(ch)
                times -= 1
        return "".join(res)


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort("tree"))
    print(s.frequencySort("cccaaa"))
    print(s.frequencySort("Aabb"))
