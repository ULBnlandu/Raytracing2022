# coding=utf-8
import math
import cmath
from coeff_transmissions import coeff_transmissions
from fonctions import distance
def ondes_transmission(plane):
    # Cette fonction a pour objectif de calculer la puissance reçue par 
    # les récepteurs en ne prennant en compte que les ondes directes et 
    # les phénomènes de transmission
    c = 299792458 # m/s
    f = 60000000000.0 #Hz
    L = c/f # lambda
    recepteurs = plane.getRecepteurs()
    for recepteur in recepteurs: # Pour chaque récepteur
        print('Le programme considère les ondes directes en ' + str(recepteur.getPosition().getx()) + '     '+str(recepteur.getPosition().gety()))
        for emetteur in plane.getEmetteurs(): # Calculer la puissance reçue par chaque emetteur
            d = distance(emetteur.getPosition(), recepteur.getPosition())
            En = (math.sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(math.pi)/L) * d))/ d
            # Il faut ajuster le calcul du champ électrique avec les coefficients de transmission =>
            En = En * coeff_transmissions(plane.getObstacles(), recepteur, emetteur)
            recepteur.increaseField(En)
    return
