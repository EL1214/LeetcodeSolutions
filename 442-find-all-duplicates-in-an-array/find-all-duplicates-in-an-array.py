class Solution(object):
    def findDuplicates(self, nums):
        seen = {}
        ans = []
        for i in nums:
            if i in seen:
                seen[i] += 1
            else:
                seen[i] = seen.get(i,0)+1
        
        for j in seen:
            if seen[j] == 2:
                ans.append(j)
        return ans
        