class Solution(object):
    def isPathCrossing(self, path):
        directions = [(-1,0),(0,1),(1,0),(0,-1)] #NESW
        row,col = 0,0
        stages = [[0,0]]
        for d in path:
            if d == "N":
                x,y = directions[0]
            elif d == "E":
                x,y = directions[1]
            elif d == "S":
                x,y = directions[2]
            else:
                x,y = directions[3]
            row += x
            col += y
            if [row,col] in stages:
                return True
            stages.append([row,col])
        return False
        
            
            




        