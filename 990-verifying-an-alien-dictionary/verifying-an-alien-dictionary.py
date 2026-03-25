class Solution(object):
    def isAlienSorted(self, words, order):
        #True #correct order
        #False #incorrect order #not enought character 
        orderdict = {}
        for i in range(len(order)):
            orderdict[order[i]]= i
        
        
        for count in range(len(words)-1):
            word1,word2 = words[count],words[count+1]
            flag = False
            for i in range(min(len(word1),len(word2))):
                if word1[i] != word2[i]:
                    if orderdict[word1[i]] > orderdict[word2[i]]:
                        return False
                    flag = True
                    break
            if len(word1) > len(word2) and flag == False:
                return False
        return True
                    
                

        