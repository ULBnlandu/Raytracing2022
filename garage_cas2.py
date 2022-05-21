# coding=utf-8
from position import Position
from obstacle import Obstacle
from emetteur import Emetteur
from coeff_reflexion import coeff_reflexion
from plane import Plane
from math import gamma, pi, cos, sin, sqrt,asin, log
import cmath
import fonctions
emetteurs = []
emetteur = Emetteur(Position(32,10), 0.001, 1.7, 73); emetteurs.append(emetteur)
start = Position(0,0)
end = Position(0,80)
mur_gauche = Obstacle(start,end,"mur garage", 4.8, 0.018, 0.15, True)
#
# Constantes du problème
epsilon0 = 8.85418782*10**(-12)
mu0 = 4 * pi * 10**(-7)
epsilonR = 4.8
sigma = 0.018
epsilon = epsilon0 * epsilonR
f = 868.3* 10**6
w = 2 * pi * f
#
#Coordonnées de l'image 1
image = fonctions.findImage(emetteur, mur_gauche)
print("Coordoonées de l'image(logiciel): " + (image).toString())
print("Coordoonées de l'image(syllabus) = (-32, 10)")
print("\n")
#Distance parcourue par l'onde
recepteur = Position(47, 65)
d = fonctions.distance(image, recepteur)
print("Distance parcourue par l'onde(logiciel)= " + str(d))
print("Distance parcourue par l'onde(syllabus) = 96,26")
print('\n')
#Calcul de l'angle d'incidence
intersection = fonctions.findIntersection(start, end, image, recepteur)
thetaI = fonctions.findThetaI(intersection, emetteur.getPosition(), mur_gauche)
print('ThetaI angle d\'incidence (logiciel) = ' + str(thetaI))
print('ThetaI angle d\'incidence (syllabus) = 0,608')
print('\n')
#Calcul de l'angle transmis
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
print('thetaT angle transmis (logiciel) = ' + str(thetaT))
print('Angle transmis (syllabus) = 0.2640')
print('\n')
# Calcul de la distance parcourue dans le milieu 
s = mur_gauche.getEpaisseur()/cos(thetaT)
print('Distance parcourue dans le matériaux(logiciel) = ' + str(s))
print('Distance parcourue dans le materiau(syllabus) = 0.155')
print('\n')
#calcul de gamma perpendiculaire 
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print('Gamma perpendiculaire (logiciel) = ' + str(gammaP))
print('Gamma perpendiculaire (syllabus) =  ' +str(complex(-0.4416, 0.0156)))
print('\n')
#calcul du coefficient de réflexion
coeff_reflexion = coeff_reflexion(emetteur, intersection, mur_gauche)
print('Coefficient de réflexion(logiciel) = ' + str(coeff_reflexion))
print('Coefficient de réflexion(syllabus) = ' + str(complex(-0.334,0.225)))
print('\n')
#Calcul du point d'intersection Pr
print('Coordonnées du point d\'intersection Pr (logiciel) = ' + intersection.toString())
print('Coordonnées du point d\'intersection (syllabus) = (0,32.28)')
print('\n')
#Calcul du point d'intersection  Pt
start = Position(0,20)
end = Position(100, 20)
mur_bas = Obstacle(start,end,"mur garage", 4.8, 0.018, 0.15, True)
Pt = fonctions.findIntersection(start, end,emetteur.getPosition(),intersection)
# Calcul de l'angle d'incidence sur le mur du bas
Pr = intersection
thetaI = fonctions.findThetaI(emetteur.getPosition(), Pr, mur_bas)
print('Angle d\'incidence sur le mur du bas (logiciel)= ' + str(thetaI))
print('Angle d\'incidence sur le mur du bas (syllabus)= 0,963')
print('\n')
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
#Distance parcourue dans le milieu
s = mur_bas.getEpaisseur()/cos(thetaT)
print('Distance parcourue dans le milieu,s (logiciel)= ' + str(s))
print('Distance parcourue dans le milieu,s (syllabus)= 0,162')
print('\n')
#gamma perpendiculaire 
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print('Gamma perpendiculaire (logiciel)= ' + str(gammaP))
print('Gamma perpendiculaire (syllabus)= (-0.562+0.0133j)')
print('\n')
# coefficient de transmission
gammaM = fonctions.gammaMilieu(epsilon, sigma)
Tm = fonctions.coefTransmission(gammaP, gammaM,s, thetaI, thetaT)
print('Coefficient de transmission (logiciel) = ' + str(Tm))
print('Coefficient de transmission (syllabus) = (0.539+0.023j)')
print('\n')
# Calcul du champ électrique
c = 299792458
L = c/f
he = L/(pi)
E2 = (10**4) * coeff_reflexion * Tm * (sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(pi)/L) * d))/ d 
print('Champ dû à cette réflexion (logiciel) = ' +str(E2) + '*10^(-4)')
print('Champ dû à cette réflexin (syllabus) =(-5,41-4,57j)* 10^(-4)')
print('\n')
puissance = complex(0.0037, -0.0016) + E2
puissance = (he*abs(puissance))**2
puissance = puissance/(8 * 73)
dBm = 10 * log(puissance/(10**(-3)), 10)
print('dBm des 2 contributions = ' + str(dBm))