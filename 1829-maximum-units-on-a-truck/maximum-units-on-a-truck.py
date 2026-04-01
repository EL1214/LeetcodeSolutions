class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        currentbox = 0
        result = 0
        for i in range(len(boxTypes)):
                box,unit = boxTypes[i]
                if currentbox < truckSize:
                    if  truckSize-currentbox > box :
                        currentbox += box
                        result += (box*unit)
                    else:
                        box = truckSize-currentbox
                        currentbox += box
                        result += (box*unit)
        return result

                
                    
                
                
        