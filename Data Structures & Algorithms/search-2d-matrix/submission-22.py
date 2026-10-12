class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if mat[-1]<target:
                continue
            else:
                if target in mat:
                    return True
        return False