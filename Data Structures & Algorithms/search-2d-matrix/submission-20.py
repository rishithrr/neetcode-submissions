class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for m in matrix:
            if m[-1]<target:
                continue
            else:
                l = 0
                r = len(m)-1
                while l<=r:
                    mid = l+((r-l)//2)
                    if target<m[mid]:
                        r = mid-1
                    elif target>m[mid]:
                        l = mid+1
                    else:
                        return True
        return False
        