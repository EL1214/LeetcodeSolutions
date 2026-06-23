class Solution(object):
    def topKFrequent(self, nums, k):
        hashmap = {}
        for i in nums:
            hashmap[i] = hashmap.get(i,0) + 1 
        
        bucket = [[] for _ in range(len(nums) + 1)]
        for n,c in hashmap.items():
            bucket[c].append(n)
        
        res = []
        for x in range(len(bucket)-1 , 0,  -1):
            for n in bucket[x]:
                res.append(n)
                if len(res) == k:
                    return res

        



        
            
            
            
                

        