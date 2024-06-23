# You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

# Return the number of connected components in the graph.

 

# Example 1:


# Input: n = 5, edges = [[0,1],[1,2],[3,4]]
# Output: 2
# Example 2:


# Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
# Output: 1
 

# Constraints:

# 1 <= n <= 2000
# 1 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai <= bi < n
# ai != bi
# There are no repeated edges.

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank=[1]*n
        
        def find(n1):
            res=n1
            while res!=parent[res]:
                parent[res]=parent[parent[res]]
                res=parent[res]
            return res
        
        def union(n1,n2):
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            if rank[p1]>rank[p2]:
                parent[p2]=p1
                rank[p1]=rank[p1]+rank[p2]
            else:
                parent[p1]=p2
                rank[p2]=rank[p2]+rank[p1]
            return 1
        
        res=n
        
        for a,b in edges:
            res=res-union(a,b)
        return res
                