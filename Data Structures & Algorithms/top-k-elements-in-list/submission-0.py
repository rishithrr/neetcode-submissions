class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}
        for num in nums:
            if num not in dic.keys():
                dic[num]=1
            else:
                dic[num]+=1
            
        res=dict(sorted(dic.items(), key=lambda key_val: key_val[1], reverse=True))
        lst=list(res.keys())
        result=[]
        for i in range(k):
            result.append(lst[i])
        return result
            

