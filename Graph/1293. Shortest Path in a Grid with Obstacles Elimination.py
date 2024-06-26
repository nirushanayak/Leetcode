# You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

# Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.

 

# Example 1:


# Input: grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# Output: 6
# Explanation: 
# The shortest path without eliminating any obstacle is 10.
# The shortest path with one obstacle elimination at position (3,2) is 6. Such path is (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3,2) -> (4,2).
# Example 2:


# Input: grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# Output: -1
# Explanation: We need to eliminate at least two obstacles to find such a walk.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 40
# 1 <= k <= m * n
# grid[i][j] is either 0 or 1.
# grid[0][0] == grid[m - 1][n - 1] == 0

from collections import deque
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        queue=deque([(0,0,k,0)]) #store the row,col,remain,step 
        seen=set()
        seen.add((0,0,k))
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        def isValid(row,col):
            return 0<=row<m and 0<=col<n

        while queue:
            r,c,remain,steps=queue.popleft()
            if r==m-1 and c==n-1:
                return steps
            for row,col in directions:
                next_r,next_c=r+row,c+col
                if isValid(next_r,next_c):
                    if grid[next_r][next_c]==0: #no Obstacle
                        if (next_r,next_c,remain) not in seen:
                            seen.add((next_r,next_c,remain))
                            queue.append((next_r,next_c,remain, steps+1))
                    elif remain and (next_r,next_c,remain-1) not in seen:
                            seen.add((next_r,next_c,remain-1))
                            queue.append((next_r,next_c,remain-1, steps+1))

        return -1