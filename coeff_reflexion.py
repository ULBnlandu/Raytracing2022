# coding=utf-8
import fonctions
from math import sin, sqrt, asin, cos, pi
import cmath
def coeff_reflexion(emetteur , intersection, obstacle):
    #Calcul de le coefficient de réflexion pour un emetteur, une intersection et un obstacle donné
    f = 60 * 10 ** 9
    #f = 868.3* 10**6
    omega = 2*pi* f
    c = 299792458
    b = omega/c # Nombre d'onde
    epsilon0 = 8.85418782 * 10 **(-12)
    epsilon = obstacle.getEpsilon()
    sigma2 = obstacle.getSigma()
    thetaI = fonctions.findThetaI(emetteur.getPosition(), intersection.getPosition(), obstacle)
    sinthetat = sqrt(epsilon0/epsilon)*sin(thetaI)
    thetaT = asin(sinthetat)
    gammaP = fonctions.GammaPerpendiculaire(epsilon0, epsilon, 0, sigma2, thetaI, thetaT)
    gammaM = fonctions.gammaMilieu(epsilon, sigma2)
    s = obstacle.getEpaisseur() / cos(thetaT)
    numerateur = gammaP * cmath.exp(- 2 * gammaM *s) * cmath.exp( complex(0,1) * b * 2 * s * sin(thetaI) * sin(thetaT))
    denominateur = 1 - (gammaP ** 2) * cmath.exp(- 2 * gammaM * s) * cmath.exp(complex(0,1) * b * 2 * s * sin(thetaI) * sin(thetaT))
    fraction = numerateur / denominateur
    coeff = gammaP - (1 - gammaP**2) * fraction
    return coeff