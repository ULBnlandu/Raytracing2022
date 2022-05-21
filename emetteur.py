# coding=utf-8
import matplotlib.pyplot as plt

class Emetteur:
    def __init__(self, position, power, gain, impedance):
        self.position = position
        self.power = power
        self.gain = gain
        self.impedance = impedance
    def plot(self):
        plt.plot(self.position.getx(), self.position.gety(), marker = "o", markersize = 6, markeredgecolor="red", markerfacecolor="red")
    
    def getPosition(self):
        return self.position

    def getPower(self):
        return self.power
    
    def getGain(self):
        return self.gain
    
    def getImpedance(self):
        return self.impedance