class Solution(object):
    def countCharacters(self, words, chars):
        q1 = {}
        length = 0
        for c in chars:
            q1[c] = q1.get(c,0)+1

        for word in words:
            q2 = {}
            for w in word:
                q2[w] = q2.get(w,0)+1
            flag = True
            for i in q2:
                if i not in q1:
                    flag = False
                elif q2[i] > q1[i]:
                    flag = False
            if flag == True:
                length += len(word)
        return length
                
            