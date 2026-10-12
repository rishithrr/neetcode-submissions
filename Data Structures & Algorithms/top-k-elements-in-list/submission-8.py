class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt = {}
        for i, v in enumerate(nums):
            dt[v] = 1 + dt.get(v, 0)
        freq = [[] for i in range(len(nums)+1)]
        for num, v in dt.items():
            freq[v].append(num)

        res = []
        for i in range(len(freq)-1, 0 , -1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res