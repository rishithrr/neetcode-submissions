class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dt={}
        for i in nums:
            dt[i]=1+dt.get(i, 0)
        lst=[]
        newlistlen=len(nums)+1
        while (newlistlen!=-1):
            lst.append([])
            newlistlen-=1
        for q,v in dt.items():
            lst[v].append(q)
            res=[]
        for lt in range(len(lst)-1,0,-1):
            for n in lst[lt]:
                res.append(n)
                if len(res)==k:
                    return res
            

            