from typing import List
from collections import defaultdict
import heapq

# leetcode 1514
# dijkstra to find shortest path in weighted graph with priority queue
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        m, graph, p = len(edges), defaultdict(list), [0] * n
        
        for i in range(m):
            n1, n2 = edges[i]
            graph[n1].append((n2, i))
            graph[n2].append((n1, i))
        print(graph, succProb)

        p[start] = 1.0
        q = [(-p[start], start)]
        while q:
            prob, cur = heapq.heappop(q)
            if cur == end:
                return -prob
            for nb, idx in graph[cur]:
                if -prob * succProb[idx] > p[nb]:
                    p[nb] = -prob * succProb[idx]
                    heapq.heappush(q, (-p[nb], nb))
        return 0
        
if __name__ == '__main__':
    sol = Solution()
    n = 3
    edges = [[0,1],[1,2],[0,2]]
    succProb = [0.5,0.5,0.2]
    start = 0
    end = 2
    print(sol.maxProbability(n, edges, succProb, start, end))
