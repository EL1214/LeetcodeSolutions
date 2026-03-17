class Solution(object):
    def largestOverlap(self, img1, img2):
        a_1 = []
        b_1 = []
        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    a_1.append([i,j])
                if img2[i][j] == 1:
                    b_1.append([i,j])
        
        d = {}
        ans = 0
        for a_x,a_y in a_1:
            for b_x,b_y in b_1:
                trans = (a_x - b_x, a_y - b_y) 
                if trans in d:
                    d[trans] +=1
                else:
                    d[trans] = 1
                ans = max(ans,d[trans])
        return ans
        
        