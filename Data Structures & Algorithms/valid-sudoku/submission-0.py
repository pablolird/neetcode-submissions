class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0 for _ in range(9)] for _ in range(9)]
        columns = [[0 for _ in range(9)] for _ in range(9)]
        squares = [[0 for _ in range(9)] for _ in range(9)]

        for i,row in enumerate(board):
            for j,cell in enumerate(row):
                if cell==".":
                    continue
                
                if rows[i][int(cell)-1]==1:
                    return False
                else:
                    rows[i][int(cell)-1]=1

                if columns[j][int(cell)-1]==1:
                    return False
                else:
                    columns[j][int(cell)-1]=1


                if squares[(i // 3) * 3 + (j // 3)][int(cell)-1]==1:
                    return False
                else:
                    squares[(i // 3) * 3 + (j // 3)][int(cell)-1]=1
        
        return True

