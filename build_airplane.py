# coding=utf-8
# Cette fonction renvoie un objet avion comme décrit 
# dans l'énnoncé du projet

from obstacle import Obstacle
from ondes_transmission import ondes_transmission
from position import Position
from emetteur import Emetteur
from plane import Plane
from ondes_reflexion import ondes_reflexion
from ondes_doubles_reflexion import ondes_doubles_reflexions
from ondes_triples_reflexions import ondes_triples_reflexions
step = 0.2
contours = [
    [(12,0), (43, 0)],
    [(43,0), (44, 1)],
    [(44,1), (44,7)],
    [(44,7), (43,8)],
    [(43,8), (12,8)],
    [(12,8), (8, 7.7384)],
    [(8, 7.7384), (5, 7.3435)],
    [(5, 7.3435), (3, 6.8076)],
    [(3, 6.8076), (1.5, 5.9416)],
    [(1.5, 5.9416), (0.5, 4.9416)],
    [(0.5, 4.9416), (0, 4.15)], 
    [(0, 4.15), (0, 4)],
    [(0, 4), (0.5, 3.0584)],
    [(0.5, 3.0584), (1.5, 2.0584)],
    [(1.5, 2.0584), (3, 1.1924)],
    [(3, 1.1924), (5, 0.6565)],
    [(5, 0.6565), (8,0.2626)],
    [(8,0.2626), (12,0)]

]
paroies_interieures = [
    [(8, 0.2626), (8, 7.7384)],
    [(12,0),(12,3)],
    [(12,8), (12,5)],
    [(20,0), (20,3)],
    [(20,8), (20,5)],
    [(38, 0), (38,3)],
    [(38,8), (38,5)],
    [(40,0), (40,3)],
    [(40, 8), (40,5)]
]
sieges_premiere_classe = [
    [(14,0), (14,3)],
    [(14, 8), (14,5)],
    [(16,0), (16,3)],
    [(16, 8), (16,5)],
    [(18,0), (18,3)],
    [(18, 8), (18,5)],
]
sieges_deuxieme_classe = [
    [(22, 0), (22,3)],
    [(22,8), (22,5)],
    [(23.5, 0), (23.5,3)],
    [(23.5,8), (23.5,5)],
    [(25, 0), (25,3)],
    [(25,8), (25,5)],
    [(26.5, 0), (26.5,3)],
    [(26.5,8), (26.5,5)],
    [(28, 0), (28,3)],
    [(28,8), (28,5)],
    [(29.5, 0), (29.5,3)],
    [(29.5,8), (29.5,5)],
    [(31, 0), (31,3)],
    [(31,8), (31,5)],
    [(32.5, 0), (32.5, 3)],
    [(32.5,8), (32.5,5)],
    [(34, 0), (34, 3)],
    [(34,8), (34,5)],
    [(35.5, 0), (35.5, 3)],
    [(35.5,8), (35.5,5)],
    [(37, 0), (37, 3)],
    [(37,8), (37,5)],

]

obstacles = []
for mur in contours:
    start = Position(mur[0][0], mur[0][1])
    end = Position(mur[1][0], mur[1][1])
    paroie = Obstacle(start,end,"GRP", 8.7, 0.868, 0.1, True)
    obstacles.append(paroie)

for paroie in paroies_interieures:
    start = Position(paroie[0][0], paroie[0][1])
    end = Position(paroie[1][0], paroie[1][1])
    paroie = Obstacle(start,end,"GRP", 8.7, 0.868, 0.1, False)
    obstacles.append(paroie)

for siege in sieges_premiere_classe:
    start = Position(siege[0][0], siege[0][1])
    end = Position(siege[1][0], siege[1][1])
    paroie = Obstacle(start,end,"plastique", 2.25, 0.003, 0.1, False)
    obstacles.append(paroie)
for siege in sieges_deuxieme_classe:
    start = Position(siege[0][0], siege[0][1])
    end = Position(siege[1][0], siege[1][1])
    paroie = Obstacle(start,end,"plastique", 2.25, 0.003, 0.1, False)
    obstacles.append(paroie)

emetteurs = []
emetteurs.append(Emetteur(Position(19,2), 0.1, 1.7, 73))
emetteurs.append(Emetteur(Position(29.5,4), 0.1, 1.7, 73))
plane = Plane(obstacles, emetteurs, step)
plane.buildRecepteurs()
ondes_transmission(plane)
# ondes_reflexion(plane)
# ondes_doubles_reflexions(plane)
# ondes_triples_reflexions(plane)
plane.plotHeatMapdBm()
plane.plotHeatMapdMbs()
#plane.plot()