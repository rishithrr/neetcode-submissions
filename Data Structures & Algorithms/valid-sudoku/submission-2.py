class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        subgrid=[set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num=board[r][c]
                if num!=".":
                    subgrid_index=(r//3)*3+(c//3)
                    if num in rows[r] or num in cols[c] or num in subgrid[subgrid_index]:
                        return False
                    rows[r].add(num)
                    cols[c].add(num)
                    subgrid[subgrid_index].add(num)
        return True