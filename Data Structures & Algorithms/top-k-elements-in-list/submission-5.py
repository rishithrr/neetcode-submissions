class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt={}
        for i in nums:
            dt[i]=1+dt.get(i,0)
        spl=[[] for i in range(len(nums)+1)]

        for ke,v in dt.items():
            spl[v].append(ke)
        res=[]
        for i in range(len(spl)-1, 0, -1):
            for n in spl[i]:
                res.append(n)
                if k==len(res):
                    return res


            

            