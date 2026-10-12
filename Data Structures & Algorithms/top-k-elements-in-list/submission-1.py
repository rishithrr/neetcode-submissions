class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=1+freq.get(num, 0)
        
        arr=[[] for _ in range(len(nums)+1)]
        for val,cnt in freq.items():
            arr[cnt].append(val)
        
        res=[]
        for i in range(len(arr)-1, 0, -1):
            for n in arr[i]:
                res.append(n)
                if len(res)==k:
                    return res
                    
    
