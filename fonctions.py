# coding=utf-8
# Stocke des fonctions reprises souvent dans le reste du code
from math import cos, sqrt
from math import pi 
from math import acos 
from cmath import exp
from math import sin
from tkinter import X
from turtle import Turtle
from position import Position
import cmath
def aligned(pos1, pos2, pos3): 
    # Renvoie true si 3 points du plan sont alignés et que le deuxième
    # point est sur le segment formé par les 2 premiers
    result = False
    vec1 = (pos2.getx() - pos1.getx(), pos2.gety() - pos1.gety())
    vec2 = ((pos3.getx() - pos2.getx(), pos3.gety() - pos2.gety()))
    min_x = min(pos1.getx(), pos3.getx())
    max_x = max(pos1.getx(), pos3.getx())
    min_y = min(pos1.gety(), pos3.gety())
    max_y = max(pos1.gety(), pos3.gety())
    sclaire = vec1[0]*vec2[1] - vec1[1]*vec2[0]
    if(sclaire == 0 and pos2.getx() <= max_x and pos2.getx() >= min_x and pos2.gety() <= max_y and pos2.gety() >= min_y):
        result = True
    return result

def isOnObstacle(obstacles, Position):
    result = False
    for obstacle in obstacles:
        start = obstacle.getStart()
        end = obstacle.getEnd()
        if(aligned(start, Position, end)):
            return True
    return result

def isInsidePlane(obstacles, position):
    result = False
    obstacle_audessus = False
    obstacle_endessous = False
    for obstacle in obstacles:
        x1 = min(obstacle.getStart().getx(), obstacle.getEnd().getx())
        x2 = max(obstacle.getStart().getx(), obstacle.getEnd().getx())
        y1 = min(obstacle.getStart().gety(), obstacle.getEnd().gety())
        y2 = max(obstacle.getStart().gety(), obstacle.getEnd().gety())
        if(position.getx() >= x1 and position.getx() <= x2):
            if(x1 == x2):
                pass
            a = (obstacle.getStart().gety()- obstacle.getEnd().gety()) / (obstacle.getStart().getx() - obstacle.getEnd().getx())
            b = obstacle.getEnd().gety() - a * obstacle.getEnd().getx()
            hauteur = a*position.getx() + b
            if(position.gety() <= hauteur):
                obstacle_audessus = True
            if(position.gety() >= hauteur):
                obstacle_endessous = True
    if(obstacle_endessous == True and obstacle_audessus == True):
        result = True
    return result

def findRanges(obstacles):
    min_x_range = 0
    max_x_range = 0 
    min_y_range = 0
    max_y_range = 0
    for paroie in obstacles:
        min_x_range_2 = min(paroie.getStart().getx(),paroie.getEnd().getx())
        min_y_range_2 = min(paroie.getStart().gety(),paroie.getEnd().gety())
        max_x_range_2 = max(paroie.getStart().getx(),paroie.getEnd().getx())
        max_y_range_2 = max(paroie.getStart().gety(),paroie.getEnd().gety())
        if(min_x_range_2 <= min_x_range):
            min_x_range = min_x_range_2
        if(min_y_range_2 <= min_y_range):
            min_y_range = min_y_range_2
        if(max_x_range_2 >= max_x_range):
            max_x_range = max_x_range_2
        if(max_y_range_2 >= max_y_range):
            max_y_range = max_y_range_2
    return min_x_range, max_x_range, min_y_range, max_y_range

def distance(pos1, pos2):
    pos1 = pos1.getPosition()
    pos2 = pos2.getPosition()
    pythagore = (pos2.getx() - pos1.getx())**2 + (pos2.gety() - pos1.gety())**2
    distance = sqrt(pythagore)
    return distance

def findIntersection(pos1, pos2, pos3, pos4):
    #Vérifier qu'on a pas des pentes infinies 
    #pos1 et 2 les point définissant l'obstacle
    # pos 3 et 4 le parcours de l'onde
    if(pos2.getx() == pos1.getx() and pos4.getx() ==  pos3.getx()): # Si les 2 droites sont horizontales
        return False
    if(pos2.getx() == pos1.getx()): # Si l'obstacle est vertical
        xIntersection = pos2.getx()
        penteOnde = ( pos4.gety() - pos3.gety() ) / ( pos4.getx() - pos3.getx() )
        pOnde = pos4.gety() - penteOnde * pos4.getx()
        yIntersection = penteOnde * xIntersection + pOnde
        intersection = Position(xIntersection, yIntersection)
        if(appartientAuxDeuxSegmentsDeDroites(pos1, pos2, pos3, pos4, intersection)):
            return intersection
        else:
            return False
    if (pos4.getx() ==  pos3.getx()): # Si le parcours est vertical 
        xIntersection = pos4.getx()
        penteObstacle = (pos2.gety() - pos1.gety())/(pos2.getx() - pos1.getx())
        pObstacle = pos2.gety() - penteObstacle * pos2.getx()
        yIntersection = penteObstacle*xIntersection + pObstacle
        intersection = Position(xIntersection, yIntersection)
        if(appartientAuxDeuxSegmentsDeDroites(pos1, pos2, pos3, pos4, intersection)):
            return intersection
        else:
            return False
    # Créer la première droite (du mur)
    penteObstacle = (pos2.gety() - pos1.gety())/(pos2.getx() - pos1.getx())
    pObstacle = pos2.gety() - penteObstacle * pos2.getx()
    # Créer la droite représentant l'onde
    penteOnde = ( pos4.gety() - pos3.gety() ) / ( pos4.getx() - pos3.getx() )
    pOnde = pos4.gety() - penteOnde * pos4.getx()
    if(penteOnde == penteObstacle):
        return False
    else:
        xIntersection = (pObstacle - pOnde) / (penteOnde - penteObstacle)
        yIntersection = penteObstacle*xIntersection + pObstacle
        intersection = Position(xIntersection, yIntersection)
        if(appartientAuxDeuxSegmentsDeDroites(pos1, pos2, pos3, pos4, intersection)):
            return intersection
        else:
            return False

def findThetaI(pos1, pos2, obstacle): # semble fonctionner
    # Trouve l'angle Theta incidient entre un obstacle 
    # et une onde. Utilise la formule du produit scalaire de 2 vecteurs 
    # pos1 correspond au recepteur / image 
    #pos2 correspond à l'emetteur / intersection
    u = (pos1.getx() - pos2.getx(), pos1.gety() - pos2.gety())
    v = (obstacle.getStart().getx() - obstacle.getEnd().getx(), obstacle.getStart().gety() - obstacle.getEnd().gety())
    if(u == (0,0)):
        print('\n')
        print(' !!!!!! BUG !!!!!!!!')
        print(u)
        print(v)
        print(pos1.getx())
        print(pos1.gety())
        print(pos2.getx())
        print(pos2.gety())
        return False

    numerateur = u[0]*v[0] + u[1] * v[1]
    denominateur = sqrt(u[0]**2 + u[1]**2)*sqrt(v[0]**2 + v[1]**2)
    cosTheta = numerateur / denominateur
    if(abs(cosTheta) > 1):
        print('BUG')
        print('\n')
        print(u)
        print('\n')
        print(v)
        print('\n')
        print(cosTheta)
        print('\n')
        cosTheta = 1
    Theta = acos(cosTheta)
    ThetaI = pi/2 - Theta
    return ThetaI

def GammaPerpendiculaire(epsilon1, epsilon2, sigma1, sigma2, thetaI, thetaT):
    # l'indice 1 fait référence au milieu incident 
    # l'indice 2 fait référence au milieu transmis
    mu0 = 4 * pi * 10**(-7)
    #f = 868.3* 10**6
    f = 60*10**9
    w = 2 * pi * f 
    Z1 = cmath.sqrt(mu0 / (epsilon1 - (complex(0,1) * sigma1)/ w) )
    Z2 = cmath.sqrt(mu0 / (epsilon2 - (complex(0,1) * sigma2)/ w) )
    GammaPerpendiculaire = (Z2*cos(thetaI) - Z1*cos(thetaT)) / (Z2 * cos(thetaI) + Z1*cos(thetaT))
    return GammaPerpendiculaire

def gammaMilieu(epsilon, sigma):
    #f = 868.3* 10**6
    f = 60 * 10**9
    omega = 2*pi* f
    mu0 = 4 * pi * 10**(-7)
    gammaM = complex(0,1) * omega * cmath.sqrt( mu0*(epsilon - (complex(0,1) * sigma)/omega ) )
    return gammaM

def coefTransmission(gammaP, gammaM, s, thetaI, thetaT):
    #f = 868.3* 10**6
    f = 60 * 10**9
    omega = 2*pi* f
    c = 299792458
    b = omega/c # Nombre d'onde
    numerateur = (1 - (gammaP ** 2))*cmath.exp( - 1 * gammaM * s)
    denominateur = 1 - (gammaP ** 2) * cmath.exp(-2*gammaM *s) * cmath.exp( complex(0,1) * b * 2 * s * sin(thetaI) * sin(thetaT))
    coeff = numerateur / denominateur
    return coeff

def findImage(emetteur, obstacle):
    # Trouve les coordoonées images de l'emetteur
    if(obstacle.getStart().getx() == obstacle.getEnd().getx()):
        xObstacle = obstacle.getStart().getx()
        xEmetteur = emetteur.getPosition().getx()
        yEmetteur = emetteur.getPosition().gety()
        DeltaX = xEmetteur - xObstacle
        image = Position(xObstacle - DeltaX, yEmetteur)
        return image
    else:
        penteObstacle = (obstacle.getStart().gety() - obstacle.getEnd().gety()) / (obstacle.getStart().getx() - obstacle.getEnd().getx())
        pObstacle = obstacle.getStart().gety() - penteObstacle * obstacle.getStart().getx()
        if(penteObstacle == 0):
            deltaY = obstacle.getStart().gety() - emetteur.getPosition().gety()
            image = Position(emetteur.getPosition().getx(), obstacle.getStart().gety() + deltaY)
            return image
        else:
            pentePerpendiculaire = -1 / penteObstacle
            pPerpendiculaire = emetteur.getPosition().gety() - pentePerpendiculaire * emetteur.getPosition().getx()
            Xintersection= (pPerpendiculaire - pObstacle) / (penteObstacle - pentePerpendiculaire)
            Yintersection = (pentePerpendiculaire * Xintersection) + pPerpendiculaire
            deltaX = (Xintersection - emetteur.getPosition().getx())
            deltaY = (Yintersection - emetteur.getPosition().gety())
            image = Position(emetteur.getPosition().getx() + deltaX, emetteur.getPosition().gety() + deltaY)
            return image

def appartientAuxDeuxSegmentsDeDroites(pos1, pos2, pos3, pos4, pos5):
    # Vérifie que la pos5 appartient bien aux 2 SEGMENTS de droites
    # pos1, pos2 
    # pos3, pos4
    appartientauxdeuxsegments = False
    x_min = min(pos1.getx(), pos2.getx())
    x_max = max(pos1.getx(), pos2.getx())
    y_min = min(pos1.gety(), pos2.gety())
    y_max = max(pos1.gety(), pos2.gety())
    if(pos5.getx() <= x_max and pos5.getx() >= x_min and pos5.gety() <= y_max and pos5.gety() >= y_min):
        x_min = min(pos3.getx(), pos4.getx())
        x_max = max(pos3.getx(), pos4.getx())
        y_min = min(pos3.gety(), pos4.gety())
        y_max = max(pos3.gety(), pos4.gety())
        if(pos5.getx() <= x_max and pos5.getx() >= x_min and pos5.gety() <= y_max and pos5.gety() >= y_min):
            appartientauxdeuxsegments = True
    return appartientauxdeuxsegments

def pointAppartientAObstacle(point, obstacle):
    aligner = aligned(obstacle.getStart(), point, obstacle.getEnd())
    res = False
    if(aligner):
        pos1 = obstacle.getStart()
        pos2 = obstacle.getEnd()
        x_min = min(pos1.getx(), pos2.getx())
        x_max = max(pos1.getx(), pos2.getx())
        y_min = min(pos1.gety(), pos2.gety())
        y_max = max(pos1.gety(), pos2.gety())
        if(point.getx() <= x_max and point.getx() >= x_min and point.gety() <= y_max and point.gety() >= y_min):
            res = True
    return res