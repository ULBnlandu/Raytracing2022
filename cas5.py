from ondes_doubles_reflexion import ondes_doubles_reflexions
from position import Position
from obstacle import Obstacle 
from emetteur import Emetteur
from plane import Plane
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
paroies = [
    [(0, 10), (20, 10)],
    [(15, 0), (15, 20)]
]
for paroie in paroies:
    start = Position(paroie[0][0], paroie[0][1])
    end = Position(paroie[1][0], paroie[1][1])
    mur = Obstacle(start,end,"GRP", 2.25, 0.003, 0.1, False)
    obstacles.append(mur)
emetteurs = []
emetteur = Emetteur(Position(10,15), 0.1, 1.7, 73); emetteurs.append(emetteur)
plane = Plane(obstacles, emetteurs, step)
plane.buildRecepteurs()
ondes_doubles_reflexions(plane)
plane.plotHeatMapdBm()
plane.plotHeatMapdMbs()