class Solution(object):
    def isHappy(self, n):
        loop = set()
        while n != 1:
            result = 0
            for i in str(n):
                result += int(i)**2
            if result in loop:
                return False
            loop.add(result)
            n = result
        return True