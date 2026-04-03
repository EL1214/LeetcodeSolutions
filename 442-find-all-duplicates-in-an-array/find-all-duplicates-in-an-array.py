class Solution(object):
    def findDuplicates(self, nums):
        seen = set()
        result = set()
        for i in nums:
            if i in seen:
                result.add(i)
            else:
                seen.add(i)
        return list(result)
        