# You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

# You are given two arrays redEdges and blueEdges where:

# redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
# blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
# Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

# Example 1:

# Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
# Output: [0,1,-1]
# Example 2:

# Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
# Output: [0,1,-1]
 

# Constraints:

# 1 <= n <= 100
# 0 <= redEdges.length, blueEdges.length <= 400
# redEdges[i].length == blueEdges[j].length == 2
# 0 <= ai, bi, uj, vj < n

from collections import defaultdict,deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph=defaultdict(list)
        result=[float(inf)]*n
        blue="B"
        red="R"
        both="Both"
        for n1,n2 in redEdges:
            graph[n1].append((n2,red))
        for n1,n2 in blueEdges:
            graph[n1].append((n2,blue))
        
        queue=deque([(0,both,0)]) #node,color,step
        seen=set()
        seen.add((0,both)) #node,color

        while queue:
            node,c,step=queue.popleft()
            result[node]=min(result[node],step)
            for neighbour,color in graph[node]:
                if (neighbour,color) not in seen:
                    if c==blue and color==red:
                        seen.add((neighbour,color))
                        queue.append((neighbour,color,step+1))
                    elif c==red and color==blue:
                        seen.add((neighbour,color))
                        queue.append((neighbour,color,step+1))
                    elif c==both:
                        seen.add((neighbour,color))
                        queue.append((neighbour,color,step+1))

        return [x if x != float("inf") else -1 for x in result]
        

#### 
from collections import defaultdict,deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        result=[float(inf)]*n
        RED=0
        BLUE=1
        graph = defaultdict(lambda: defaultdict(list))
        for x, y in redEdges:
            graph[RED][x].append(y)
        for x, y in blueEdges:
            graph[BLUE][x].append(y)
        
        ans = [float("inf")] * n
        queue = deque([(0, RED, 0), (0, BLUE, 0)])
        seen = {(0, RED), (0, BLUE)}
        
        while queue:    
            node, color, steps = queue.popleft()
            ans[node] = min(ans[node], steps)
            
            for neighbor in graph[color][node]:
                if (neighbor, 1 - color) not in seen:
                    seen.add((neighbor, 1 - color))
                    queue.append((neighbor, 1 - color, steps + 1))
        
        return [x if x != float("inf") else -1 for x in ans]