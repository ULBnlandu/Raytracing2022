# coding=utf-8
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def getx(self):
        return self.x
    def gety(self):
        return self.y
    def toString(self):
        return "(X= "  + str(self.x) + "," + "Y= " + str(self.y) + ")"
    def getPosition(self):
        return self