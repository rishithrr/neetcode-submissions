class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles)==h:
            return max(piles)

        l=1
        r=max(piles)
        res=max(piles)
        while(l<=r):
            mid=l+(r-l)//2
            sum=0
            for num in piles:
                sum+=math.ceil(num/mid)
            if sum<=h:
                r=mid-1
                res=min(res, mid)
            else:
                l=mid+1
        return res
