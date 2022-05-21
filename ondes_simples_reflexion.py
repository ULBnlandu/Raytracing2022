# coding=utf-8
from xml.etree.ElementPath import find
from fonctions import findImage
from fonctions import findIntersection
from coeff_transmissions import coeff_transmissions
from coeff_reflexion import coeff_reflexion
from fonctions import distance
from position import Position
import math
import cmath
def ondes_simples_reflexion(plane):
    # Cette fonction a pour objectif de déterminer pour chaque 
    # récepteur du problème la puissance reçue des récepteurs
    # due aux ondes ayant subies strictement une seule réflexion
    # On procède par la méthode des images et on considère les éventuelles transmissions

    for recepteur in plane.getRecepteurs():
        #print('Le programme considère la réflexion simple en ' + str(recepteur.getPosition().getx()) + '     '+str(recepteur.getPosition().gety()))
        for emetteur in plane.getEmetteurs():
            obstacle = plane.getObstacles()[0]
            image = findImage(emetteur, obstacle) # Existe toujours
            intersection = findIntersection(obstacle.getStart(), obstacle.getEnd(), image, recepteur.getPosition())
            transmission1 = coeff_transmissions(plane.getObstacles(), intersection, emetteur)
            transmission2 = coeff_transmissions(plane.getObstacles(), recepteur, intersection)
            c = 299792458.0 # m/s
            f = float(60*10**9)#Hz
            L = c/f # lambda
            d = distance(image, recepteur.getPosition())
            En = (math.sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(math.pi)/L) * d))/ d #Le champ 
            reflexion = coeff_reflexion(emetteur.getPosition(), intersection, obstacle)
            Er = En * reflexion * transmission1 * transmission2
            recepteur.increaseField(Er)



