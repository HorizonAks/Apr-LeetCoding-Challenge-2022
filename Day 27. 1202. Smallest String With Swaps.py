#Day 27
#1202. Smallest String With Swaps
#might give TLE

class UnionFind:
    def __init__(self,size):
        self.group = [0]*size
        self.rank = [0]*size
        
        for i in range(size):
            self.group[i] = i
    
    def find(self,node):
        if self.group[node] != node:
            self.group[node] = self.find(self.group[node])
        return self.group[node]
    
    def union(self,node1,node2):
        group1 = self.find(node1)
        group2 = self.find(node2)
        
        if group1 == group2:
            return False
        
        if self.rank[group1] > self.rank[group2]:
            self.group[group2] = group1
        elif self.rank[group1] < self.rank[group2]:
            self.group[group1] = group2
        else:
            self.group[group2] = group1
            self.rank[group1] += 1
        return True
    
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        #n = len(pairs)
        m = len(s)
        uf = UnionFind(m)
        
        for x,y in pairs:
            uf.union(x,y)
        
        res = list(s)
        for i in range(m):
            mini = i
            for j in range(i+1,m):
                if res[j] < res[mini] and uf.find(i) == uf.find(j):
                    mini = j
            res[i],res[mini] = res[mini],res[i]
            
        return "".join(res)
