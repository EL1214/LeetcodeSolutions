class Solution(object):
    def tictactoe(self, moves):
        rows = [0] * 3
        cols = [0] * 3
        di = 0
        andi = 0
        count = 0
        player = 1
        for r,c in moves:
            rows[r] += player
            cols[c] += player
            if r == c:
                di += player
            if r+c == 2:
                andi += player
            if 3 in (rows[r],cols[c],di,andi):
                return "A"
            if -3 in (rows[r],cols[c],di,andi):
                return "B"
            player *= -1
            count += 1
        if count == 9:
            return "Draw"
        return "Pending"
            
        
            

            
                
            