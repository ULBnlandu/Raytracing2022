import fonctions
from coeff_transmissions import coeff_transmissions
from coeff_reflexion import coeff_reflexion
import math
import cmath
def ondes_triples_reflexions(plane):
    for recepteur in plane.getRecepteurs():
        print('Le programme considère la réflexion triple en ' + str(recepteur.getPosition().getx()) + '     '+str(recepteur.getPosition().gety()))
        for emetteur in plane.getEmetteurs():
            for obstacle1 in plane.getObstacles():
                for obstacle2 in plane.getObstacles():
                    for obstacle3 in plane.getObstacles():
                        # Le deuxième obstacle ne peut pas être le même que le premier
                        # mais à priori le troisième peut etre le même que le premier 
                        if(obstacle1.getStart() != obstacle2.getStart() and obstacle1.getEnd() != obstacle2.getEnd() and obstacle1 != obstacle3):
                            image1 =  fonctions.findImage(emetteur, obstacle1)
                            image2 = fonctions.findImage(image1, obstacle2)
                            image3 = fonctions.findImage(image2, obstacle3)
                            intersection3 = fonctions.findIntersection(obstacle3.getStart(), obstacle3.getEnd(), image3, recepteur.getPosition())
                            if(intersection3):
                                intersection2 = fonctions.findIntersection(obstacle2.getStart(), obstacle2.getEnd(), image2, intersection3)
                                if(intersection2):
                                    intersection1 = fonctions.findIntersection(obstacle1.getStart(), obstacle1.getEnd(), image1, intersection2)
                                    if(intersection1): # Si l'intersection existe
                                        transmission1 = coeff_transmissions(plane.getObstacles(), intersection1, emetteur)
                                        transmission2 = coeff_transmissions(plane.getObstacles(), intersection1, intersection2)
                                        transmission3 = coeff_transmissions(plane.getObstacles(), intersection2, intersection3)
                                        transmission4 = coeff_transmissions(plane.getObstacles(), intersection3, emetteur)
                                        
                                        c = 299792458 # m/s
                                        f = 60*10**9 #Hz
                                        L = c/f # lambda
                                        reflexion1 = coeff_reflexion(emetteur, intersection1, obstacle1)
                                        reflexion2 = coeff_reflexion(intersection1, intersection2, obstacle2)
                                        reflexion3 = coeff_reflexion(emetteur, intersection2, obstacle3)
                                        d = fonctions.distance(image3, recepteur.getPosition())
                                        En = (math.sqrt(60 * emetteur.getGain() * emetteur.getPower())* cmath.exp(-1 * complex(0,1) * (2*(math.pi)/L) * d))/ d #Le champ
                                        Er = En * reflexion1 * reflexion2 * reflexion3 * transmission1 * transmission2 * transmission3 * transmission4
                                        recepteur.increaseField(Er)



    return