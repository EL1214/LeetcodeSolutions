class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        new = []
        for i in range(len(nums)-k,len(nums)):
            new.append(nums[i])            
        for j in range(0,len(nums)-k):
            new.append(nums[j])
        nums[:]= new #keep the content but change the order 
        return new
       
       #efficient one
'''k = k % len(nums) #for when k is larger than the length of the array
num[:]= num[-k:] + num[:-k]'''
        
        