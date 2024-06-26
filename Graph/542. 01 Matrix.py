# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

# The distance between two adjacent cells is 1.

 

# Example 1:


# Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
# Output: [[0,0,0],[0,1,0],[0,0,0]]
# Example 2:


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]
 

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= m, n <= 104
# 1 <= m * n <= 104
# mat[i][j] is either 0 or 1.
# There is at least one 0 in mat.

from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue=deque()
        seen=set()
        m=len(mat)
        n=len(mat[0])
        directions=[(1,0),(0,1),(0,-1),(-1,0)]
        for row in range(m):
            for col in range(n):
                if mat[row][col]==0:
                    queue.append((row,col,1))
                    seen.add((row,col))

        def isValid(row,col):
            return 0<=row<m and 0<=col<n and mat[row][col] == 1

        #bfs
        while queue:
            row,col,step=queue.popleft()
            for r,c in directions:
                next_r,next_c=row+r,col+c
                if isValid(next_r,next_c) and (next_r,next_c) not in seen:
                    queue.append((next_r,next_c,step+1))
                    seen.add((next_r,next_c))
                    mat[next_r][next_c]=step

        return mat