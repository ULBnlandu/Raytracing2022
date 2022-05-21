# coding=utf-8
import matplotlib.pyplot as plt

class Recepteur:
    def __init__(self, position, mutable):
        self.position = position
        self.reception = 0.0
        self.E = 0.0
        self.mutable = mutable
        
    def plot(self):
        plt.plot(self.position.getx(), self.position.gety(), marker = "o", markersize = 1, markeredgecolor="black", markerfacecolor="black")

    def getPosition(self):
        return self.position
        
    def getReception(self):
        return self.reception
    def getField(self):
        return self.E
    def increaseReception(self, power):
        if (self.mutable == True):
            self.reception += power
        return
    def increaseField(self, field):
        if(self.mutable == True):
            self.E = self.E + field
        return