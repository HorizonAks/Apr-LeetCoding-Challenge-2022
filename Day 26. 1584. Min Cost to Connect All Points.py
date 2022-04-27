#Day 26
#1584. Min Cost to Connect All Points


#Simple Kruskal Algorithm
class unionFind:
    def __init__(self, size):
        self.parents = [0] *size
        self.rank = [0] * size

        for i in range(size):
            self.parents[i] = i
            
    def find(self,node):
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def union(self, node1, node2):
        parent1 = self.find(node1)
        parent2 = self.find(node2)

        if parent1 == parent2:
            return False
        if self.rank[parent1] > self.rank[parent2]:
            self.parents[parent2] = parent1
        elif self.rank[parent1] < self.rank[parent2]:
            self.parents[parent1] = parent2
        else:
            self.parents[parent2] = parent1
            self.rank[parent1] += 1

        return True
    
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        edges = []
        for i in range(n):
            for j in range(i+1,n):
                edges.append((abs(points[i][0]-points[j][0]) + abs(points[i][1]-points[j][1]),i,j))
        edges.sort()

        uf = unionFind(n)
        mst_cost = 0
        edgesUsed = 0
        for w, node1, node2 in edges:
            if uf.union(node1,node2):
                mst_cost+=w
                edgesUsed+=1
                if edgesUsed == n - 1:
                    break
                    
        return mst_cost
