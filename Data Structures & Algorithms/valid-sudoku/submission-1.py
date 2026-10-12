class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        col=[set() for _ in range(9)]
        subgrid=[set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if board[i][j]!=".":
                    subgrid_index=(i//3)*3+(j//3)
                    num=board[i][j]
                    if num in rows[i] or num in col[j] or num in subgrid[subgrid_index]:
                        return False
                    rows[i].add(num)
                    col[j].add(num)
                    subgrid[subgrid_index].add(num)
        return True