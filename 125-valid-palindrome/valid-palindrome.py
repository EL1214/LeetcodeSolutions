class Solution(object):
    def isPalindrome(self, s):
        #Convert
        s = s.lower()
        news = ""
        for i in s:
            if i.isalnum():
                news += i
        
        Spointer = 0
        Epointer = len(news)-1
        while Spointer <= Epointer:
            if news[Spointer] != news[Epointer]:
                return False
            else:
                Spointer += 1
                Epointer -= 1
        return True

 