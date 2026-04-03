class Solution(object):
    def subarraySum(self, nums, k):
        total = 0
        count = 0
        seen = {0:1}
        for i in nums:
            total += i 
            if (total-k) in seen:
                count += seen[total-k]
                print(count)
            seen[total]= seen.get(total,0)+1
        return count


                
        
            
        
                
        