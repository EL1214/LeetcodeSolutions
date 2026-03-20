class Solution(object):
    def islandPerimeter(self, grid):
        total = 0
        row = len(grid)
        col = len(grid[0])
        direction = [(-1,0),(1,0),(0,-1),(0,1)] #u,d,l,r
        for i in range(row):
            for j in range(col):
                    if grid[i][j] ==1:
                        for x,y in direction:
                            nrow,ncol = i+x,j+y
                            if nrow < 0 or nrow > row-1 or ncol < 0 or ncol > col-1:
                                total += 1
                            elif grid[nrow][ncol]==0:
                                total += 1
        return total
                            