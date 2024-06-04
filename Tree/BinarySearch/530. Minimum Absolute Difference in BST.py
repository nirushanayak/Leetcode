# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values=[]
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            values.append(root.val)
            dfs(root.right)
        dfs(root)
        ans=float("inf")
        for i in range(1,len(values)):
            ans=min(ans,values[i]-values[i-1])
        return ans