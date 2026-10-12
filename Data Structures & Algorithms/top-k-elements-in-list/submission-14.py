class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i, v in enumerate(nums):
            freq[v] = freq.get(v, 0) + 1
        ifreq = defaultdict(list)
        for key, v in freq.items():
            ifreq[v].append(key)
        bucket = [[] for i in range(len(nums)+1)]
        for key, v in ifreq.items():
            for n in v:
                bucket[key].append(n)
        res = []
        for i in range(len(nums), -1, -1):
            for n in bucket[i]:
                res.append(n)
                print(res)
                if len(res)==k:
                    print("hit")
                    return res        