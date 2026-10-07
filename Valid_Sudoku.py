# Time Complexity : O(81)
# Space Complexity : O(1)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Your code here along with comments explaining your approach
# Using HashSet. Iterate over the board and assign the row, col and box values as i as row index, j as col index, i//3 as row and j //3 as col for box to know which box grid it belongs
# Then check if the cell is empty and row, col and box value is not in Hashset then add it to HashSet
# If it is already in HashSet return False


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return False
        seen = set()
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] != ".":
                    num = board[i][j]
                    row = num + " in row " + str(i)
                    col = num + " in col " + str(j)
                    box = num + " in box " + str(i//3) + "-" + str(j//3)
                    if row in seen or col in seen or box in seen:
                        return False
                    else:
                        seen.add(row)
                        seen.add(col)
                        seen.add(box)
        return True
                    
