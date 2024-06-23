# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

 

# Example 1:


# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.
# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen=set()
        ans=[0]
        result=0
        directions=[(1,0),(0,1),(-1,0),(0,-1)]

        def isValid(row,col):
            if  0<= row < len(grid) and 0<=col< len(grid[0]) and grid[row][col]:
                return True
            return False

        def dfs(row,col):
            for r,c in directions:
                next_r,next_c=row+r,col+c
                if isValid(next_r,next_c) and (next_r,next_c) not in seen:
                    seen.add((next_r,next_c))
                    ans[0]=ans[0]+1
                    dfs(next_r,next_c)


       
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1 and (i,j) not in seen:
                    ans[0]=1
                    seen.add((i,j))
                    dfs(i,j)
                    result=max(result,ans[0])

        return result
                
        