from random import shuffle, randrange
import sys
from itertools import product


def make_maze(num, name):
    w = num
    vis = [[0] * w + [1] for _ in range(w)] + [[1] * (w + 1)]
    ver = [[".."]+["#."] * (w-1) + ['#']]+[["#."] * w + ['#']
                                           for _ in range(w-2)]+[["#."] * (w) + ["."]] + [[]]
    hor = [[".#"]+["##"] * (w-1) + ['#']]+[["##"] * w + ['#']
                                           for _ in range(w-1)] + [["#"] * (2*w-1) + ['#.']]

    def debugPrint():
        s = ""
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        print(s)

    def Unvisitedcells(matrix):
        # Si accès aux éléments et aux indices
        return [valeur for line in matrix for valeur in line if valeur == 0]
# for i_line, line in enumerate(matrice):
#     for i_col, col in enumerate(line):
       # unvisitedcells=[]
       # for i in range(len(matrix)):
        #    for j in range(len(matrix)):
        #        if matrix[i][j]==0:
        #            unvisitedcells.append(matrix[i][j])
       # return unvisitedcells

    def createmaze(x, y):
        stack = []
        stack.append([x, y])
        while len(stack):
            # print(vis)
            coord = stack.pop(0)
            x = coord[0]
            y = coord[1]
            vis[y][x] = 1
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if xx in range(-1, w+1) and yy in range(-1, w+1):
                    newcell = [xx, yy]
                    if vis[yy][xx] == 1 and (xx, yy) != d[3]:
                        continue

                    if vis[yy][xx] == 1 and (xx, yy) == d[3] and len(Unvisitedcells(vis)) != 0:
                        if (len(newcell) > 0):
                            stack.append(newcell)
                        break
                    elif vis[yy][xx] == 1 and (xx, yy) == d[3] and len(Unvisitedcells(vis)) == 0:
                        continue
                    if xx == x:
                        hor[max(y, yy)][x] = "#."
                        if (len(newcell) > 0):
                            stack.append(newcell)
                        break

                    if yy == y:
                        ver[y][max(x, xx)] = ".."
                        if (len(newcell) > 0):
                            stack.append(newcell)
                        break
                elif len(Unvisitedcells(vis)) != 0:
                    if xx == x and y > 0:
                        stack.append([x, y-1])
                    if xx == x and y < 0:
                        stack.append([x, y+1])
                    if yy == y and x > 0:
                        stack.append([x-1, y])
                    if yy == y and x < 0:
                        stack.append([x+1, y])
                    break

   # def go_pasrec(x, y, maze, size):
  #  stack = []
   # stack.append([x, y])
    # while (len(stack) > 0):
 #   x = stack[-1][0]
 #   y = stack[-1][1]
 #   newcell = go(x, y, maze, size)
  #  if (len(newcell) > 0):
  #      stack.append(newcell)
       # else:
       #     stack.pop()

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        ths.write(s)
        ths.close()
  #  print(vis)
    createmaze(randrange(w), randrange(w))
    print(vis)
    debugPrint()
    mazeWrite(name)


num = int(input('Entrer la taille de maze: '))
name = input('Entrer le nom de maze: ')
make_maze(num, name)
