#Day 13.
#59. Spiral Matrix II

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        rows = [0]*n
        res = []
        for i in range(n):
            res.append(rows.copy())
        directions = ((0,1),(1,0),(0,-1),(-1,0))
        
        visited = set()
        
        def isvalid(i,j):
            if 0 <= i < n and 0 <= j < n:
                return True
            return False
        def dfs(i,j,n,k):
            nr,nc = i,j
            res[nr][nc]=n
            #n+=1
            visited.add((nr,nc))
            d = 0
            cond = True
            while(cond):
                #print(res,d)
                if d > 3:
                    d = 0
                #print(res,d)
                for m in range(k-1):
                    nr,nc = nr+directions[d][0],nc+directions[d][1]
                    #print(nr,nc,m)
                    if (nr,nc) in visited:
                        nr,nc = nr-directions[d][0],nc-directions[d][1]
                        break
                    #print(res)
                    n+=1
                    res[nr][nc]=n
                    visited.add((nr,nc))
                d+=1
                for x in res:
                    if 0 in x:
                        cond = True
                        break
                    cond = False
                if not cond:
                    break
                    
        dfs(0,0,1,n)
        return res
