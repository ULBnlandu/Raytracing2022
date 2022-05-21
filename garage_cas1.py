# coding=utf-8
from position import Position
from obstacle import Obstacle
from emetteur import Emetteur
from plane import Plane
from math import pi, cos, sin, sqrt,asin, log
import cmath
import fonctions

emetteurs = []
emetteur = Emetteur(Position(32,10), 0.001, 1.7, 73); emetteurs.append(emetteur)
# On cherche à resoudre le problème "du garage", vérifions les valeurs retournées par le logiciel
epsilon0 = 8.85418782*10**(-12)
mu0 = 4 * pi * 10**(-7)
epsilonR = 4.8
sigma = 0.018
epsilon = epsilon0 * epsilonR
f = 868.3* 10**6
w = 2 * pi * f
# 
Zm = cmath.sqrt(mu0 / (epsilon - (complex(0,1) * sigma)/ w) )
res = complex(171.57, 6.65)
print("Zm = " + str(Zm))
print("Resulat du sylla" +str(res))
print("Différence de leurs normes" + str(abs(Zm) - abs(res)))
print('\n')
#
gammaM = fonctions.gammaMilieu(epsilon, sigma)
print("gamma milieu = " + str(gammaM))
res = complex(1.55, 39.90)
print("Résultat du sylla = " + str(res))
print("Différence de leurs normes = " +str(abs(gammaM) - abs(res)))
print('\n')
#
recepteur = Position(47, 65)
distance = fonctions.distance(emetteur,recepteur)
print("Distance = " + str(distance))
print("Résulat du sylla = 57")
print('\n')
#
recepteur = Position(47, 65)
obstacle = [(0,20), (100, 20)]
start = Position(obstacle[0][0], obstacle[0][1])
end = Position(obstacle[1][0], obstacle[1][1])
mur = Obstacle(start,end,"mur", 4.8, 0.018, 0.15, True)
thetaI = fonctions.findThetaI(recepteur.getPosition(),emetteur.getPosition(), mur)
print("Angle d'incidence = " + str(thetaI * 180/pi))
print("Résulat du sylla = 15,2551")
print('\n')
#
sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
thetaT = asin(sinthetat)
costhetaT = cos(thetaT)
print("cos(thetaT) = " + str(costhetaT))
print("Résulat du sylla = 0,9928")
print('\n')
#
s = 0.15 / cos(thetaT)
s_sylla = 0.151 
print("Distance dans le matériau = " + str(s))
print("Résultat du sylla = 0,151m")
print('\n')
#
gammaPerpendiculaire = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma, thetaI, thetaT)
res = complex(-0.362, 0.0165)
print("Gamma perpendiculaire = " + str(gammaPerpendiculaire))
print("Résultat du sylla = " + str(res))
print("Différence" +str(abs(gammaPerpendiculaire) - abs(res)))
print('\n')
Tm = fonctions.coefTransmission(gammaPerpendiculaire, gammaM, s_sylla, thetaI, thetaT)
res = complex(0.69, 0.23)
print("Coefficient de transmission = " + str(Tm))
print("Résulat du sylla = " + str(res))
print('\n')
#
c = 299792458
d = distance
L = c/f
he = L/(pi)
En = Tm * (sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(pi)/L) * d))/ d
print("Champ du à l'onde de transmission = " + str(En))
En_sylla = complex(0.0037, -0.0016)
print("Champ calculé dans le syllabus = " + str(En_sylla))
print("\n")
#
puissance = puissance = (he*abs(En))**2
puissance = puissance / (8 * 73)
print("Puissance perçue = " + str(puissance))
print("Puissance du sylla = 3.33*10^(-10)")
print("\n")
#
dBm = 10 * log(puissance/(10**(-3)), 10)
print('dBm = ' + str(dBm))
print("dBm calculé dans le sylla = -64.77")
print("\n")