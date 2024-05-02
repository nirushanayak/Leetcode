# Given an m x n matrix, return all elements of the matrix in spiral order.

 

# Example 1:


# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
# Example 2:


# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left,right=0,len(matrix[0])
        top,bottom=0,len(matrix)
        res=[]
        while(left<right and top<bottom):
            #move right
            for i in range(left,right):
                res.append(matrix[top][i])
            top=top+1

            #move bottom
            for i in range(top,bottom):
                res.append(matrix[i][right-1])
            right=right-1

            if not (left<right and top< bottom):
                break

            #move left
            for i in range(right-1,left-1,-1):
                res.append(matrix[bottom-1][i])
            bottom=bottom-1

            #move top
            for i in range(bottom-1,top-1,-1):
                res.append(matrix[i][left])
            left=left+1
                
        return res


            
