class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        new = []
        for i in range(len(nums)-k,len(nums)):
            new.append(nums[i])            
        for j in range(0,len(nums)-k):
            new.append(nums[j])
        nums[:]= new #otherwise the order in the original array wont change 
        return new
       
        
        