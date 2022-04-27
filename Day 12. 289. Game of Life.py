#Day 12.
#289. Game of Life

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        simulate the problem
        """
        gen = []
        for row in board:
            gen.append(row.copy())
        
        directions = ((0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1))
        
        def isvalid(i,j):
            return True if 0 <= i < len(board) and 0 <= j < len(board[0]) else False
        
        for i in range(len(gen)):
            for j in range(len(gen[0])):
                neighbours = 0
                for d in directions:
                    nr,nc = i+d[0],j+d[1]
                    if not isvalid(nr,nc): continue
                    if gen[nr][nc] == 1:
                        neighbours +=1
                if gen[i][j] == 1:
                    if neighbours < 2 or neighbours > 3:
                        board[i][j] = 0 
                else:
                    if neighbours == 3:
                        board[i][j] = 1
        
                        
