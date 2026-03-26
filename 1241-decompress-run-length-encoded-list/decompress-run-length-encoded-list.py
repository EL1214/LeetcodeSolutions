class Solution(object):
    def decompressRLElist(self, nums):
        new = []
        index = 0
        while index <= len(nums)-2:
            freq = nums[index]
            number = nums[index+1]
            for _ in range(freq):
                new.append(number)
            index += 2
        return new
        