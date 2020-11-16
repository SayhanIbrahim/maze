import time
labyrinthe = []
ListeDonees = open("15.txt").read().split()


for ligne in ListeDonees:
    Listecaratere = []
    for caractere in ligne:
        Listecaratere.append(caractere)
    labyrinthe.append(Listecaratere)
visited = [[0] * len(labyrinthe) for _ in range(len(labyrinthe))]


class Noeuds:
    def __init__(self, position, parent):

        self.gcost = 0
        self.hcost = 0
        self.fcost = 0
        self.position = position
        self.parent = parent

    def __eq__(self, autre):
        return self.position == autre.position

    def __lt__(self, autre):  # pour le rengement par ordre
        return self.fcost < autre.fcost


def test_validite(i, j):
    return (i >= 0 and i <= (len(labyrinthe)-1)) and (j >= 0 and j <= (len(labyrinthe)-1))


def calcul_distance_carree(x1, x2, y1, y2):
    return ((x2-x1)**2+(y2-y1)**2)


def recheche_chemin_court(labyrinthe, entree, sortie):

    ListeCellulesAvisiter = []
    noeud_entree = Noeuds(entree, None)
    noeud_sortie = Noeuds(sortie, None)
    ListeCellulesAvisiter.append(noeud_entree)

    while len(ListeCellulesAvisiter) > 0:
        ListeCellulesAvisiter.sort()
        noeud_actuel = ListeCellulesAvisiter.pop(0)
        (a, b) = noeud_actuel.position
        visited[a][b] = 1
        if noeud_actuel == noeud_sortie:
            solution = []
            while noeud_actuel is not None:
                solution.append(noeud_actuel.position)
                noeud_actuel = noeud_actuel.parent
            return solution[::-1]
        (x, y) = noeud_actuel.position
        ListeVoisins = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
        for element in ListeVoisins:
            (i, j) = element
            if test_validite(i, j):
                if(labyrinthe[i][j] == '#'):
                    continue
                noeud_enfant = Noeuds(element, noeud_actuel)
                (c, d) = noeud_enfant.position
                if visited[c][d] == 1:
                    continue
                noeud_enfant.gcost = calcul_distance_carree(
                    noeud_entree.position[0], noeud_enfant.position[0], noeud_entree.position[1], noeud_enfant.position[1])
                noeud_enfant.hcost = calcul_distance_carree(
                    noeud_enfant.position[0], noeud_sortie.position[0], noeud_enfant.position[1], noeud_sortie.position[1])
                noeud_enfant.fcost = noeud_enfant.gcost + noeud_enfant.hcost
                SituationChemincourt = True
                for element in ListeCellulesAvisiter:
                    if (noeud_enfant == element and noeud_enfant.fcost >= element.fcost):
                        SituationChemincourt = False
                    break
                if SituationChemincourt == True:
                    ListeCellulesAvisiter.append(noeud_enfant)


print("Start : %s" % time.ctime())

entree = (0, 0)
sortie = (len(labyrinthe)-1, len(labyrinthe)-1)
solution = recheche_chemin_court(labyrinthe, entree, sortie)
if len(solution) == 0:
    print("no path found!")

for path in solution:
    (x, y) = path
    # labyrinthe[x][y]='\033[93m'+'o'+'\033[0m'
    labyrinthe[x][y] = 'o'

for i in range(len(labyrinthe)):
    for j in range(len(labyrinthe)):
        if labyrinthe[i][j] == '.':
            labyrinthe[i][j] = '*'
nom = input('Entrer le nom (et éventuellement le chemin) du fichier de sortie: ')
ths = open(f"{nom}.txt", "a")
for line in labyrinthe:
    line2 = ''.join(line)
   # print (line2)
    ths.write(line2)
ths.close()


print("End : %s" % time.ctime())
