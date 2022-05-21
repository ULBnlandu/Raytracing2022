# coding=utf-8
# Cette classe représente les obstacles du problèmes
# En particulier, elle permet de les réprésenter sur le plan 
# et d'accéder à leurs caractéristiques

import matplotlib.pyplot as plt

class Obstacle:
    def __init__(self, start, end, type, er, sigma, epaisseur, edge):
        self.start = start
        self.end = end
        self.type = type
        self.er = er
        self.sigma = sigma
        self.epaisseur = epaisseur
        self.edge = edge
    def plot(self):
        x = [self.start.getx(), self.end.getx()]
        y = [self.start.gety(), self.end.gety()]
        if(self.type == "GRP"):
            plt.plot(x,y, color = 'black')
        if(self.type == "plastique"):
            plt.plot(x,y, color = 'blue')
        return

    def getStart(self):
        return self.start
        
    def getEnd(self):
        return self.end

    def getEpaisseur(self):
        return self.epaisseur

    def getEpsilonRelatif(self):
        return self.er

    def getEpsilon(self):
        return self.er * 8.85418782 * 10 **(-12)

    def getSigma(self):
        return self.sigma

    def isEdge(self):
        return self.edge
    
    def getType(self):
        return self.type
