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
                    if(obstacle1.getStart() != obstacle2.getStart() and obstacle1.getEnd() != obstacle2.getEnd()): # and obstacle1.isEdge()==False and obstacle2.isEdge()==False 
                        image2 = fonctions.findImage(image1, obstacle2)
                        intersection2 = fonctions.findIntersection(obstacle2.getStart(), obstacle2.getEnd(), image2, recepteur.getPosition())
                        if(intersection2 != False):
                            intersection1 = fonctions.findIntersection(obstacle1.getStart(), obstacle1.getEnd(), image1, intersection2)
                            x_min = min(image1.getx(), intersection2.getx())
                            x_max = max(image1.getx(), intersection2.getx())
                            y_min = min(image1.gety(), intersection2.gety())
                            y_max = max(image1.gety(), intersection2.gety())

                        # Il faut vérifier que l'intersection 1 appartient bien au segment de droite image 1 - intersection2
                        if(intersection1): # si elle existe :)
                            if(intersection1.getx() >= x_min and intersection1.getx() <= x_max and intersection1.gety() <= y_max and intersection1.gety() >= y_min):
                                # Ensuite l'intersection 2 doit elle appartenir à la droite image2 - recepteur
                                x_min = min(image2.getx(), recepteur.getPosition().getx())
                                x_max = max(image2.getx(), recepteur.getPosition().getx())
                                y_min = min(image2.gety(), recepteur.getPosition().gety())
                                y_max = max(image2.gety(), recepteur.getPosition().gety())
                                if(intersection2):
                                    if(intersection2.getx() >= x_min and intersection2.getx() <= x_max and intersection2.gety() <= y_max and intersection2.gety() >= y_min):
                                        # Si c'est le cas on ajoute les coefficients
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



