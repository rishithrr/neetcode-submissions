class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if mat[-1]<target:
                continue
            l=0
            r=len(mat)-1
            while(l<=r):
                mid=l+(r-l)//2
                if mat[mid]<target:
                    l=mid+1
                elif mat[mid]>target:
                    r=mid-1
                else:
                    return True
        return False
        