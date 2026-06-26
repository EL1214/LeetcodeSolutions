class Solution(object):
    def twoSum(self, numbers, target):
        start , end = 0, len(numbers)-1
        while start < end:
            while numbers[start] + numbers[end] > target:
                end -= 1
            while numbers[start] + numbers[end] < target:
                start += 1
            if numbers[start] + numbers[end] == target:
                return [ start + 1, end + 1]
            
            
