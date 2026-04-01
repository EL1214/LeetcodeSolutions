class Solution(object):
    def arraySign(self, nums):
        result = 1
        for i in nums:
            result *= i
        if result > 0:
            return 1
        elif result < 0:
            return -1
        else:
            return 0
        