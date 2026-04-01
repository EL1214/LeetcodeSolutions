class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        result = 0
        for i in range(len(boxTypes)):
            if truckSize <= 0:
                break
            
            box,unit = boxTypes[i]
            box = min(box,truckSize)
            result += (box*unit)
            truckSize -= box
        return result
                
                
                    
                
                
        