# coding=utf-8
from ondes_transmission import ondes_transmission
from position import Position
from obstacle import Obstacle
from emetteur import Emetteur 
from plane import Plane
from ondes_reflexion import ondes_reflexion
step = 0.2
contours = [
    [(0,0), (20, 0)],
    [(20,0), (20, 20)],
    [(20,20), (0,20)],
    [(0,20), (0,0)]
]

obstacles = []
for contour in contours:
    start = Position(contour[0][0], contour[0][1])
    end = Position(contour[1][0], contour[1][1])
    paroie = Obstacle(start,end,"GRP", 8.7, 0.868, 0.1, True)
    obstacles.append(paroie)
    

emetteurs = []
emetteur = Emetteur(Position(19,10), 0.1, 1.7, 73); emetteurs.append(emetteur)
plane = Plane(obstacles, emetteurs, step)
plane.buildRecepteurs()
ondes_reflexion(plane)
plane.plotHeatMapdBm()
plane.plotHeatMapdMbs()