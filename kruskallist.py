from random import choice
from itertools import product
import sys
import copy
import faulthandler
from PIL import Image, ImageDraw


faulthandler.enable()
sys.setrecursionlimit(10 ** 9)


def make_maze(num, name):
    w = num
    m = w*w
    vis = []
    vis2 = [m//5, m*35//100, m//2, m*65//100,
            m*75//100, m*85//100, m*9//10, m*95//100]
    count = 0
    for i in range(0, w):
        liste = []
        while len(liste) > 0:
            liste.pop()
        for i in range(count, count + w):
            liste.append(i)
            count += 1
        vis.append(liste)

    listofwalls = list(product(range(0, w - 1), range(0, w - 1), range(2)))
    for i in range(w - 1):
        listofwalls.append(((w - 1), i, 0))
        listofwalls.append((i, (w - 1), 1))

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

    def cellidchanger(l, k):
        for i in range(w):
            for j in range(w):
                if k < l:
                    if vis[i][j] == l:
                        vis[i][j] = k
                else:

                    if vis[i][j] == k:
                        vis[i][j] = l

    def walk(x, y, vh):
        i = 0
        while i < w**2:
            j = len(listofwalls)
            # print('len of list of walls', j)
            if j > 1:
                (x, y, vh) = choice(listofwalls)
                k = vis[y][x]
                if vh == 0:
                    l = vis[y + 1][x]
                else:
                    l = vis[y][x + 1]
                if l == k:
                    try:
                        listofwalls.remove((x, y, vh))
                    except:
                        continue
                elif vh == 0:
                    hor[y + 1][x] = "#."
                    cellidchanger(l, k)
                    i = i+1
                else:
                    ver[y][x + 1] = ".."
                    cellidchanger(l, k)
                    i = i+1
                try:
                    listofwalls.remove((x, y, vh))
                except:
                    continue
                if i in vis2:
                    wallcleaner()
            else:
                debugPrint()
                mazeWrite(name)
                break

    def wallcleaner():
        liste = copy.deepcopy(listofwalls)
        print(len(liste))
        for (j, i, vh) in liste:
            k = vis[i][j]
            try:
                l = vis[i][j + 1]
                if k == l:
                    try:
                        listofwalls.remove((j, i, 1))
                        # print(j, i, 1, "erased")
                    except:
                        continue
            except:
                continue
        for (j, i, vh) in liste:
            k = vis[i][j]
            try:
                m = vis[i + 1][j]
                if k == m:
                    try:
                        listofwalls.remove((j, i, 0))
                        # print(j, i, 0, "erased")
                    except:
                        continue
            except:
                continue

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += "".join(a + ["\n"] + b + ["\n"])
        ths.write(s)
        ths.close()
        createJPG()
        # print(listofwalls)
        # debugPrint()
        for line in vis:
            print(line)
        exit()

    def createJPG():
        large = 3*(w)
        img = Image.new('RGB', (large, large), (255, 255, 255))
        t = large//w
        draw = ImageDraw.Draw(img)
        draw.line((large-2, 0, large-2, large-2), fill=(0, 0, 0), width=1)
        draw.line((0, large-2, large-2, large-2), fill=(0, 0, 0), width=1)
        draw.line((0, 0, large-2, 0), fill=(0, 0, 0), width=1)
        draw.line((0, 0, 0, large-2), fill=(0, 0, 0), width=1)

        for y in range(w):
            for x in range(w):
                try:
                    if ver[y][x] == "#.":
                        draw.line((t*x, t*y, t*x, t*y+t),
                                  fill=(0, 0, 0), width=1)
                    if hor[y][x] == "##":
                        draw.line((t*x, t*y, t*x+t, t*y),
                                  fill=(0, 0, 0), width=1)
                except:
                    pass
        img.show()
        img.save(f"{name}.jpg")

    (x, y, vh) = choice(listofwalls)
    walk(x, y, vh)
    mazeWrite(name)


num = int(input("Entrer la taille de maze: "))
name = input("Entrer le nom de maze: ")
make_maze(num, name)
