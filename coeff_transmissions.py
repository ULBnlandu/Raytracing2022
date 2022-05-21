# coding=utf-8
from math import asin
from math import sin
from math import cos
from math import sqrt
from math import pi
import fonctions 

def coeff_transmissions(obstacles, recepteur, emetteur):
    # Cette fonction prend en paramètre la liste
    # des obstacles, le recepteur et emetteur considéré,
    # et renvoie le coefficient de transmission assossié
    # recepeteur sur le mur ? 

    coef = 1
    for obstacle in obstacles:
        pos1 = obstacle.getStart()
        pos2 = obstacle.getEnd()
        pos3 = emetteur.getPosition()
        pos4 = recepteur.getPosition()
        intersection = fonctions.findIntersection(pos1, pos2, pos3, pos4)
        if(intersection and fonctions.pointAppartientAObstacle(intersection, obstacle) == False): # Si les segments se touchent
            #Si l'intersection est pile poil sur l'obstacle on ne doit pas considérer la transmission !!
            epsilon0 = 8.85418782 * 10 **(-12)
            epsilon = obstacle.getEpsilon()
            sigma2 = obstacle.getSigma()
            thetaI = fonctions.findThetaI(recepteur.getPosition(), emetteur.getPosition(), obstacle)
            sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
            thetaT = asin(sinthetat)
            GammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma2, thetaI, thetaT)
            gammaM = fonctions.gammaMilieu(epsilon, sigma2)
            s = obstacle.getEpaisseur() / cos(thetaT)
            transmission = fonctions.coefTransmission(GammaP, gammaM, s, thetaI, thetaT)
            coef = coef*transmission
    return coef