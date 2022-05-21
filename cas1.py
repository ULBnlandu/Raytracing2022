# coding=utf-8
#Ce code execute une fonction donnant une représentation
# du cas simplifié de 1 emetteur dans l'avion en ne considérant que les ondes directes (sans transmissions ou réflexions)
from position import Position
from obstacle import Obstacle
from emetteur import Emetteur 
from plane import Plane
from ondes_directes import ondes_directes

step = 0.2
contours = [
    [(0,0), (20, 0)],
    [(20,0), (20, 20)],
    [(20,20), (0,20)],
    [(0,20), (0,0)]
]
obstacles = []
for paroie in contours:
    start = Position(paroie[0][0], paroie[0][1])
    end = Position(paroie[1][0], paroie[1][1])
    paroie = Obstacle(start,end,"GRP", 8.7, 0.868, 0.1, True)
    obstacles.append(paroie)

emetteurs = []
emetteur = Emetteur(Position(10,10), 0.1, 1.7, 73); emetteurs.append(emetteur)
plane = Plane(obstacles, emetteurs, step)
plane.buildRecepteurs()
ondes_directes(plane)
plane.plotHeatMapdBm()
plane.plotHeatMapdMbs()
#plane.plot()

