# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def isValid(row,col):
            if row>=0 and row<r and col>=0 and col<c and grid[row][col]=="1":
                return True
            return False

        def dfs(row,col):
            for r,c in directions:
                next_row,next_col=row+r,col+c
                if isValid(next_row,next_col) and (next_row,next_col) not in seen:
                    seen.add((next_row,next_col))
                    dfs(next_row,next_col)
        
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        r=len(grid)
        c=len(grid[0])
        seen=set()
        ans=0
        for row in range(r):
            for col in range(c):
                if grid[row][col]=="1" and (row,col) not in seen:
                    ans+=1
                    seen.add((row,col))
                    dfs(row,col)
        return ans