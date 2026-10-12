class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)
        dt = {}
        for num in nums:
            dt[num] = 1 + dt.get(num, 0)
        for key, val in dt.items():
            freq[val].append(key)
        print(freq)
        bucket = [[] for i in range(len(nums)+1)]
        for key, val in freq.items():
            bucket[key]=val
            print(bucket)

        res = []
        for b in range(len(bucket)-1 , 0, -1):
            for num in bucket[b]:
                res.append(num)
                if k == len(res):
                    return res
