class ParkingSystem(object):

    def __init__(self, big, medium, small):
        self.big = big #1
        self.medium = medium #2
        self.small = small #3
        

    def addCar(self, carType):
        if carType == 1:
            if self.big == 0:
                return False
            else:
                self.big -= 1
                return True
        if carType == 2:
            if self.medium == 0:
                return False
            else:
                self.medium -= 1
                return True
        else:
            if self.small == 0:
                return False
            else:
                self.small -= 1
                return True

            
        


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)