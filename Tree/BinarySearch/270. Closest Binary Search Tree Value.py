# Given the root of a binary search tree and a target value, return the value in the BST that is closest to the target. If there are multiple answers, print the smallest.

 

# Example 1:


# Input: root = [4,2,5,1,3], target = 3.714286
# Output: 4
# Example 2:

# Input: root = [1], target = 4.428571
# Output: 1
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# 0 <= Node.val <= 109
# -109 <= target <= 109

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        result=[float("inf"),0]
        def dfs(node):
            if not node:
                return
            if abs(node.val-target)<=result[0]:
                if abs(node.val-target)==result[0]:
                    if node.val<result[1]:
                        result[1]=node.val
                else:
                    result[1]=node.val
                result[0]=abs(node.val-target)

            if node.val<=target:
                return dfs(node.right)
            else:
                return dfs(node.left)
        dfs(root)
        return result[1]


        