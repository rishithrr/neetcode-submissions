class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for mat in matrix:
            if not mat[-1]<target:
                return target in mat
        return False