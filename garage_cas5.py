# coding=utf-8
from position import Position
from obstacle import Obstacle
from emetteur import Emetteur
from coeff_reflexion import coeff_reflexion
from plane import Plane
from math import gamma, pi, cos, sin, sqrt,asin, log
import cmath
import fonctions
emetteur = Emetteur(Position(32,10), 0.001, 1.7, 73)
start = Position(0,0)
end = Position(0,80)
mur_gauche = Obstacle(start,end,"mur garage", 4.8, 0.018, 0.15, True)
start = Position(0,80)
end = Position(100, 80)
mur_haut = Obstacle(start, end, "mur garage", 4.8, 0.018, 0.15, True)
start = Position(0,20)
end = Position(100, 20)
mur_bas = Obstacle(start, end, "mur garage", 4.8, 0.018, 0.15, True)
recepteur = Position(47, 65)
#Constantes du problème
epsilon0 = 8.85418782*10**(-12)
mu0 = 4 * pi * 10**(-7)
epsilonR = 4.8
sigma = 0.018
epsilon = epsilon0 * epsilonR
f = 868.3* 10**6
w = 2 * pi * f
c = 299792458
L = c/f
he = L/(pi)
#Coordoonées de l'image 1:
image1 = fonctions.findImage(emetteur, mur_haut)
print('Coordonnées de l\'image1 (logiciel) =' + image1.toString())
print('\n')
#Coordoonées de l'image2:
image2 = fonctions.findImage(image1, mur_bas)
print('Coordonnées de l\'image 2 (logiciel)= ' + image2.toString())
print('\n')
#Coordoonées du point Pr2
Pr2 = fonctions.findIntersection(mur_bas.getStart(), mur_bas.getEnd(), image2, recepteur.getPosition())
print('Coordonné de l\'intersection Pr2 (logiciel) = ' + Pr2.toString())
print('\n')
#Coordoonées du point PR1
Pr1 = fonctions.findIntersection(mur_haut.getStart(), mur_haut.getEnd(), image1, Pr2)
print('Coordonnées de l\'intersection Pr1 (logiciel) = ' + Pr1.toString())
print('\n') 
#Coordonnée du point Pt
Pt = fonctions.findIntersection(mur_bas.getStart(), mur_bas.getEnd(), emetteur.getPosition(),Pr1)
print('Coordonées du point d\'intersection Pt (logiciel) = ' + Pt.toString())
print('\n')
#
# Calcul du coefficient de transmission
# Calcul de l'angle d'incidence 
thetaI = fonctions.findThetaI(emetteur.getPosition(), Pr1, mur_bas)
print('Angle d\'incidence pour transmission (logiciel)= ' + str(thetaI))
print('\n')
# Angle transmis 
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
print('Angle transmis pour la transmission(logiciel)= ' + str(thetaT))
print('\n')
# distance parcourue dans le materiau
s = mur_bas.getEpaisseur() / cos(thetaT)
print("Distance parcourue dans le materiaux (logiciel) = " + str(s))
print('\n')
#Gamma perpendiculaire 
gammaM = fonctions.gammaMilieu(epsilon, sigma)
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print("Gamma perpendiculaire, transmission (logiciel)= " +str(gammaP))
print('\n')
#Coefficient de transmission
Tm = fonctions.coefTransmission(gammaP, gammaM, s, thetaI, thetaT)
print("Coefficient de transmission (logiciel)= " + str(Tm))
print('------------------------------------------')
print('\n')
#
#Calcul du coefficient de la première réflexion
# Calcul de l'angle d'incidence
thetaI = fonctions.findThetaI(Pr1,emetteur.getPosition(), mur_haut)
print('thetaI angle d\'incidence, première réflexion (logiciel) = ' + str(thetaI))
print('\n')
# Calcul de l'angle transmsis 
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
print('thetaT l\'angle transmis, première réflexion (logiciel)= ' + str(thetaT))
print('\n')
# calcul de s
s = mur_haut.getEpaisseur() / cos(thetaT)
print("Distance parcourue dans le materiaux (logiciel) = " + str(s))
print('\n')
#gamma perpendiculaire et gamma M 
gammaM = fonctions.gammaMilieu(epsilon, sigma)
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print("Gamma perpendiculaire, première réflexion (logiciel)= " +str(gammaP))
print('\n')
#coefficient de réflexion
Reflexion1 = coeff_reflexion(emetteur, Pr1, mur_haut)
print('Coefficient de la première réflexion (logiciel) = ' + str(Reflexion1))
print('------------------------------------------')
print('\n')
#
#Caluls du coefficient de la deuxième réflexion
#thetaI
thetaI = fonctions.findThetaI(recepteur.getPosition(),image2, mur_bas)
print('thetaI angle d\'incidence, deuxième réflexion (logiciel) = ' + str(thetaI))
#Calcul de l'angle transmis
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
print('thetaT l\'angle transmis, deuxième réflexion (logiciel)= ' + str(thetaT))
#calcul de s
s = mur_gauche.getEpaisseur() / cos(thetaT)
print("Distance parcourue dans le materiaux (logiciel) = " + str(s))
#gamma perpendiculaire et gamma M 
gammaM = fonctions.gammaMilieu(epsilon, sigma)
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print("Gamma perpendiculaire, deuxième réflexion (logiciel)= " +str(gammaP))
#coefficient de réflexion
Reflexion2 = coeff_reflexion(recepteur, image2, mur_bas)
print('Coefficient de la Deuxième réflexion (logiciel) = ' + str(Reflexion2))
print('\n')
#Calcul du champ total
d = fonctions.distance(image2, recepteur.getPosition())
E4 = (sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(pi)/L) * d))/ d
E4 = Tm*Reflexion1*Reflexion2*E4
print('Champ perçu par l\'onde (logiciel) = ' + str(E4*10**4) + "*10^-4")