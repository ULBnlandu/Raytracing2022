# coding=utf-8
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from position import Position
import fonctions
from recepteur import Recepteur
from emetteur import Emetteur
import math
class Plane:
    def __init__(self, obstacles, emetteurs, step):
        self.obstacles = obstacles
        self.emetteurs = emetteurs
        self.step = step
        self.recepteurs = []

    def plot(self):
        plt.figure(figsize=(20,5)) # Redimmensionner l'affichage pour y voir plus clair
        for obstacle in self.obstacles:
            obstacle.plot()
        for emetteur in self.emetteurs:
            emetteur.plot()
        for recepteur in self.recepteurs:
            recepteur.plot()

        plt.margins(0.1, 0.1)
        plt.show()
        plt.close()
        return

    def plotHeatMapdBm(self):
        c = 299792458 # m/s
        f = 60000000000.0 #Hz
        L = c/f # lambda
        he = L/(math.pi)
        min_x_range, max_x_range, min_y_range, max_y_range = fonctions.findRanges(self.obstacles)
        i = int(min_x_range/self.step)
        j = int(min_y_range/self.step)
        max_i = int(max_x_range/self.step)
        max_j = int(max_y_range/self.step)
        Puissance = []
        for recepteur in self.recepteurs: # d'abord on crée un tableau des puissances perçues dans l'avion
            puissance = (he*abs(recepteur.getField()))**2
            puissance = puissance / (8 * 73)
            Puissance.append(puissance)
        tableau = []
        conteur = 0
        # Ensuite on crée un tableau des dBm
        while(j < max_j):
            row = []
            while(i < max_i):
                dBm = Puissance[conteur]
                if(dBm != 0):
                    dBm = 10 * math.log(dBm/(10**(-3)), 10)
                row.append(dBm)
                conteur += 1
                i += 1
            tableau.append(row)
            i = int(min_x_range/self.step)
            j+= 1
        plt.figure(figsize=(20,5))
        tableau = np.array(tableau)
        hm=plt.imshow(tableau)
        plt.colorbar(hm)
        #plt.clim(-53,-200)
        for obstacle in self.obstacles:
            x = [obstacle.getStart().getx() * 1/self.step, obstacle.getEnd().getx()* 1/self.step]
            y = [obstacle.getStart().gety()* 1/self.step, obstacle.getEnd().gety()* 1/self.step]
            if(obstacle.getType() == "plastique"):
                plt.plot(x, y, color= 'white')
            if(obstacle.getType() == "GRP"):
                plt.plot(x, y, color= 'black')
        plt.gca().invert_yaxis()
        plt.show()
        return tableau

    def plotHeatMapdMbs(self):
        c = 299792458 # m/s
        f = 60000000000.0 #Hz
        L = c/f # lambda
        he = L/(math.pi)
        min_x_range, max_x_range, min_y_range, max_y_range = fonctions.findRanges(self.obstacles)
        i = int(min_x_range/self.step)
        j = int(min_y_range/self.step)
        max_i = int(max_x_range/self.step)
        max_j = int(max_y_range/self.step)
        debits = []
        for recepteur in self.recepteurs:
            puissance = (he*abs(recepteur.getField()))**2
            puissance = puissance / (8 * 73)
            if(puissance != 0):
                dBm = 10 * math.log(puissance/(10**(-3)), 10)
            else:
                dBm = -10000000000.0
            pente = (4620-27.5)/(-53+78)
            p = 4620 - (pente)*(-53)
            debit = pente * dBm + p
            if(debit < 27.5):
                debit = 0
            if(debit > 4620):
                debit = 4620
            debits.append(debit)
        tableau = []
        conteur = 0
        while(j < max_j):
            row = []
            while(i < max_i):
                debit = debits[conteur]

                row.append(debit)
                conteur += 1
                i += 1
            tableau.append(row)
            i = int(min_x_range/self.step)
            j+= 1
        plt.figure(figsize=(20,5))
        tableau = np.array(tableau)
        hm=plt.imshow(tableau)
        plt.colorbar(hm)
        plt.clim(0,4620)
        for obstacle in self.obstacles:
            x = [obstacle.getStart().getx() * 1/self.step, obstacle.getEnd().getx()* 1/self.step]
            y = [obstacle.getStart().gety()* 1/self.step, obstacle.getEnd().gety()* 1/self.step]
            if(obstacle.getType() == "plastique"):
                plt.plot(x, y, color= 'white')
            if(obstacle.getType() == "GRP"):
                plt.plot(x, y, color= 'black')
        plt.gca().invert_yaxis()
        plt.show()
        return tableau  

    def getObstacles(self):
        return self.obstacles

    def getRecepteurs(self):
        return self.recepteurs

    def buildRecepteurs(self):
        # D'abord trouver la range qu'on va parcourir 
        min_x_range, max_x_range, min_y_range, max_y_range = fonctions.findRanges(self.obstacles)
        # Une fois qu'on a trouvé le domaine on parcours les points pour vérifier qu'ils ne sont pas des murs

        points_x = int((max_x_range - min_x_range)/ self.step)
        points_y = int((max_y_range - min_y_range)/ self.step)
        i = int(min_x_range/self.step)
        j = int(min_y_range/self.step)
        max_i = int(max_x_range/self.step)
        max_j = int(max_y_range/self.step)
        while(j < max_j):
            i = int(min_x_range/self.step)
            while(i < max_i):
                position = Position(i*self.step + (self.step)/2, j*self.step + (self.step)/2)
                #if(fonctions.isOnObstacle(self.obstacles, position) == False): # and fonctions.isInsidePlane(self.obstacles, position) == True
                self.recepteurs.append(Recepteur(position, True))          
                i += 1

            j += 1
        return 

    def getEmetteurs(self):
        return self.emetteurs