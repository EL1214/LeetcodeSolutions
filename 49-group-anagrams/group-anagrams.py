class Solution(object):
    def groupAnagrams(self, strs):
        hashmap = defaultdict(list)
        for m in strs:
            count = [0] * 26
            for n in m:
                count[ord(n) -ord("a")]+= 1
            
            hashmap[tuple(count)].append(m)
        return hashmap.values()




            
        

        
        