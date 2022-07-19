import time
from collections import defaultdict, deque
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # union and find have time complexity O(1)
        class DSU:
            def __init__(self, n): self.p = list(range(n))
            def union(self, x, y): self.p[self.find(x)] = self.find(y)
            def find(self, x):
                if x != self.p[x]: self.p[x] = self.find(self.p[x])
                return self.p[x]
        dsu, res, groups = DSU(len(s)), [], defaultdict(list)
        for x,y in pairs: 
            dsu.union(x,y)

        for i in range(len(s)): 
            groups[dsu.find(i)].append(s[i])
        print(dsu.p)
        for group_id in groups.keys(): 
            groups[group_id].sort(reverse=True)
        for i in range(len(s)): 
            res.append(groups[dsu.find(i)].pop())
        return ''.join(res)


if __name__ == '__main__':
    sol = Solution()
    s = "dcab"
    pairs = [[0,3],[1,2],[0,2]]
    # s = "dcab"
    # pairs = [[0, 3], [1, 2]]
    print(pairs)
    print(sol.smallestStringWithSwaps(s, pairs))
