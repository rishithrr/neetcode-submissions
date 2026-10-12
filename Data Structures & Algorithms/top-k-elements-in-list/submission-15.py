class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        bucket = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        for key, val in freq.items():
                bucket[val].append(key)
        
        res = []
        for i in range(len(nums), -1, -1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res        