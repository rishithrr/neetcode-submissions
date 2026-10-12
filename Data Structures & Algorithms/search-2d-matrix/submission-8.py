class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for lt in matrix:
            if target not in lt:
                continue
            else:
                return True
        return False
        
        