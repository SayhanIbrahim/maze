from random import shuffle, choice
from itertools import product
import sys


sys.setrecursionlimit(150000)


def make_maze(num, name):
    w = num
    vis = []
    vis2 = [[0] * w for _ in range(w)]
    count = 0
    for i in range(0, w):
        liste = []
        while len(liste) > 0:
            liste.pop()
        for i in range(count, count + w):
            liste.append(i)
            count += 1
        vis.append(liste)
    controllist = list(product(range(w), repeat=2))

    ver = (
        [[".."] + ["#."] * (w - 1) + ["#"]]
        + [["#."] * w + ["#"] for _ in range(w - 2)]
        + [["#."] * (w) + ["."]]
        + [[]]
    )
    hor = (
        [[".#"] + ["##"] * (w - 1) + ["#"]]
        + [["##"] * w + ["#"] for _ in range(w - 1)]
        + [["#"] * (2 * w - 1) + ["#."]]
    )

    def debugPrint():
        s = ""
        for (a, b) in zip(hor, ver):
            s += "".join(a + ["\n"] + b + ["\n"])
        print(s)

    def counterzeros():
        if vis == vis2:
            mazeWrite(name)
        else:
            return True

    def cellchanger(l, k):
        for i in range(w):
            for j in range(w):
                if k < l:
                    if vis[i][j] == l:
                        vis[i][j] = k
                        # controllist.remove((j, i))
                        # if l == 0:
                        try:
                            controllist.remove((j, i))
                        except:
                            continue
                else:
                    if vis[i][j] == k:
                        vis[i][j] = l
                        # controllist.remove((j, i))
                        # if k == 0:
                        try:
                            controllist.remove((j, i))
                        except:
                            continue
                # try:
                #     controllist.remove((j, i))
                # except:
                #     continue

        # print("*" * 20)
        # for line in vis:
        #     print(line)
        # debugPrint()

    def walk(x, y):
        while counterzeros():
            k = vis[y][x]
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            if (x + 1) == w:
                d.remove((x + 1, y))
            if (y + 1) == w:
                d.remove((x, y + 1))
            if (x - 1) == -1:
                d.remove((x - 1, y))
            if (y - 1) == -1:
                d.remove((x, y - 1))
            shuffle(d)
            xx, yy = d[0]
            l = vis[yy][xx]
            if l == k:
                (x, y) = choice(controllist)
                walk(x, y)
            if xx == x:
                hor[max(y, yy)][x] = "#."
            if yy == y:
                ver[y][max(x, xx)] = ".."
            cellchanger(l, k)
            (x, y) = choice(controllist)
            walk(x, y)

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += "".join(a + ["\n"] + b + ["\n"])
        ths.write(s)
        ths.close()
        print(controllist)
        debugPrint()
        # for line in vis:
        #     print(line)
        exit()

    (x, y) = choice(controllist)
    walk(x, y)


num = int(input("Entrer la taille de maze: "))
name = input("Entrer le nom de maze: ")
make_maze(num, name)
