# coding=utf-8
import fonctions
from coeff_transmissions import coeff_transmissions
from coeff_reflexion import coeff_reflexion
import math
import cmath
def ondes_doubles_reflexions(plane):
    # Cette fonction a pour objectif de déterminer pour chaque 
    # récepteur du problème la puissance reçue des récepteurs
    # due aux ondes ayant subies strictement deux réflexions
    # On procède par la méthode des images et on considère les éventuelles transmissions
    for recepteur in plane.getRecepteurs():
        print('Le programme considère la réflexion double en ' + str(recepteur.getPosition().getx()) + '     '+str(recepteur.getPosition().gety()))
        for emetteur in plane.getEmetteurs():
            for obstacle1 in plane.getObstacles():
                image1 = fonctions.findImage(emetteur, obstacle1)
                for obstacle2 in plane.getObstacles():
                    # vérifier qu'on est pas entrain de considérer le même obstacle
                    if(obstacle1.getStart() != obstacle2.getStart() and obstacle1.getEnd() != obstacle2.getEnd()):
                        image2 = fonctions.findImage(image1, obstacle2)
                        intersection2 = fonctions.findIntersection(obstacle2.getStart(), obstacle2.getEnd(), image2, recepteur.getPosition())
                        if(intersection2):
                            intersection1 = fonctions.findIntersection(obstacle1.getStart(), obstacle1.getEnd(), image1, intersection2)
                            if(intersection1):
                                transmission1 = coeff_transmissions(plane.getObstacles(), intersection1, emetteur)
                                transmission2 = coeff_transmissions(plane.getObstacles(), intersection1, intersection2)
                                transmission3 = coeff_transmissions(plane.getObstacles(), intersection2, recepteur)
                                c = 299792458 # m/s
                                f = 60*10**9 #Hz
                                L = c/f # lambda
                                reflexion1 = coeff_reflexion(emetteur, intersection1, obstacle1)
                                reflexion2 = coeff_reflexion(recepteur, intersection2, obstacle2)
                                d = fonctions.distance(image2, recepteur.getPosition())
                                En = (math.sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(math.pi)/L) * d))/ d #Le champ
                                Er = En * reflexion1 * reflexion2 * transmission1 * transmission2 * transmission3 
                                recepteur.increaseField(Er)
    return



