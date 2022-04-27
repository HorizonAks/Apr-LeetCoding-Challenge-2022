#Day 11.
#1260. Shift 2D Grid

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m,n = len(grid),len(grid[0])
        """
        if k is greater than m*n then to avoid
        unnecessary rotations, rotate grid 
        k%(m*n) times
        """
        k = k%(m*n)
        while(k!=0):
            #last element in the grid
            last = grid[m-1][n-1]
            #rotate one row at a time
            for i in range(m-1,0,-1):
                for j in range(n-1,0,-1):
                    grid[i][j] = grid[i][j-1]
                grid[i][0] = grid[i-1][n-1]
            for j in range(n-1,0,-1):
                grid[0][j] = grid[0][j-1]
            grid[0][0] = last
            k-=1
        return grid
