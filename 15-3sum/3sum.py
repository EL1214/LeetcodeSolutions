class Solution(object):
    def threeSum(self, nums):
        nums = sorted(nums)
        
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            start, end = i + 1 , len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                else:
                    res.append([nums[i],nums[start],nums[end]])
                    start += 1
                    end -= 1
                    while nums[start] == nums[start-1] and start < end:
                        start += 1
        return res
                


        