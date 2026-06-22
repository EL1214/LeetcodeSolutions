class Solution(object):
    def twoSum(self, nums, target):
        hashmap = {}
        for i in range(len(nums)):
            ans = target - nums[i]
            if ans in hashmap:
                return [hashmap[ans],i]
            else:
                hashmap[nums[i]] = i
        
        

                


