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
#Coordoonées de l'image 
image = fonctions.findImage(emetteur.getPosition(), mur_haut)
print('Coordoonées de l\'image (logiciel) = ' + image.toString())
print('\n')   
#Distance parcourue par l'onde
d = fonctions.distance(image, recepteur)
print('distance parcourue par l\'onde (logiciel)= '+ str(d))
print('\n')
#Point d'intersection Pr
Pr = fonctions.findIntersection(mur_haut.getStart(), mur_haut.getEnd(), image, recepteur.getPosition())
print('Intersection Pr (logiciel) = ' + Pr.toString())
print('\n')
#Point d'intersection Pt
Pt = fonctions.findIntersection(mur_bas.getStart(), mur_bas.getEnd(), emetteur.getPosition(), recepteur.getPosition())
print('Point d\'intersection Pt(logiciel) = ' + Pt.toString())
print('\n')
# Angle d'incidence sur le mur du bas 
thetaI = fonctions.findThetaI(emetteur.getPosition(), Pr, mur_bas)
print('Angle d\'incidence sur le mur du bas (logiciel)= ' + str(thetaI))
print('\n')
# Angle transmis
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
print('Angle transmis (logiciel)= ' + str(thetaT))
print('\n')
# Distance parcourue dans le milieu
s = mur_bas.getEpaisseur()/cos(thetaT)
print('s, distance parcourue dans le milieu (logiciel)= '+str(s))
print('\n')
# Gamma perpendiculaire
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print('Gamma perpendiculaire, transmission(logiciel)= ' + str(gammaP))
print('\n')
# Coefficient de transmission
gammaM = fonctions.gammaMilieu(epsilon, sigma)
Tm = fonctions.coefTransmission(gammaP, gammaM, s, thetaI, thetaT)
print("Coefficient de transmission (logiciel)= " + str(Tm))
print('\n')

# Angle d'incidence sur le mur du haut
thetaI = fonctions.findThetaI(emetteur.getPosition(), Pr, mur_haut)
print('Angle d\'incidence sur le mur du haut (logiciel) =' + str(thetaI))
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
# s
s = mur_haut.getEpaisseur() / cos(thetaT)
print('Distance parcourue dans le materiaux(logiciel)= ' + str(s))
print('\n')
# Gamma perpendiculaire 
gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
print('Gamma perpendiculaire, réflexion(logiciel)= ' + str(gammaP))
print('\n')
#gamma milieu 
gammaM = fonctions.gammaMilieu(epsilon , sigma)
reflexion = coeff_reflexion(emetteur, Pr, mur_haut)
print("Coefficient de réflexion (logiciel) = " + str(reflexion))
print('\n')
#
E = (sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(pi)/L) * d))/ d
E3 = reflexion*Tm*E
print('E3 (logiciel)= ' + str(E3))