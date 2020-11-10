from random import choice
from itertools import product
import sys
import copy
import faulthandler

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

    idmatrix = list(product(range(0, w), range(0, w)))
    dictionary = dict(zip(list(range(m)), idmatrix))
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

    def cellidchanger2(l, k):
        element1 = dictionary[k]
        element2 = dictionary[l]
        liste = []
        if k < l:
            if type(element1) is list:
                for i in range(len(element1)):
                    z = element1[i]
                    liste.append(z)
            else:
                liste.append(dictionary[k])
            if type(element2) is list:
                for i in range(len(element2)):
                    z = element2[i]
                    liste.append(z)
            else:
                liste.append(dictionary[l])
            dictionary[k] = liste
            del dictionary[l]
        else:
            if type(element1) is list:
                for i in range(len(element1)):
                    z = element1[i]
                    liste.append(z)
            else:
                liste.append(dictionary[k])
            if type(element2) is list:
                for i in range(len(element2)):
                    z = element2[i]
                    liste.append(z)
            else:
                liste.append(dictionary[l])
            dictionary[l] = liste
            del dictionary[k]

    def valuefinder(x, y):
        val_list = copy.deepcopy(list(dictionary.values()))
        key_list = copy.deepcopy(list(dictionary.keys()))
        for l in val_list:
            if type(l) is list:
                for i in range(len(l)):
                    if ((x, y)) in l:
                        indis = val_list.index(l)
                        idnumber = key_list[indis]
                        return(idnumber)
                        break
            elif l == (x, y):
                indis = val_list.index(l)
                idnumber = key_list[indis]
                return(idnumber)
                break

    def walk(x, y, vh):
        i = 0
        while i < w**2:
            j = len(dictionary)
            print('len of dictionary:', j)
            if j > 1:
                (x, y, vh) = choice(listofwalls)
                k = valuefinder(x, y)
                if vh == 0:
                    l = valuefinder(x, y+1)
                else:
                    l = valuefinder(x+1, y)
                if l == k:
                    try:
                        listofwalls.remove((x, y, vh))
                    except:
                        continue
                elif vh == 0:
                    hor[y + 1][x] = "#."
                    cellidchanger2(l, k)
                    i = i+1
                else:
                    ver[y][x + 1] = ".."
                    cellidchanger2(l, k)
                    i = i+1
                try:
                    listofwalls.remove((x, y, vh))
                except:
                    continue
            else:
                debugPrint()
                mazeWrite(name)
                break

    def wallcleaner2():
        liste = copy.deepcopy(listofwalls)
        # print(len(liste))
        for (x, y, vh) in liste:
            k = valuefinder(x, y)
            try:
                l = valuefinder(x+1, y)
                if k == l:
                    try:
                        listofwalls.remove((x, y, 1))
                        print(x, y, 1, "erased")
                    except:
                        continue
            except:
                continue
        for (x, y, vh) in liste:
            k = valuefinder(x, y)
            try:
                m = valuefinder(x, y+1)
                if k == m:
                    try:
                        listofwalls.remove((x, y, 0))
                        print(x, y, 0, "erased")
                    except:
                        continue
            except:
                continue

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += "".join(a + ["\n"] + b + ["\n"])
        print(dictionary)
        ths.write(s)
        ths.close()
        # print(listofwalls)
        debugPrint()
        # for line in vis:
        #     print(line)
        exit()

    (x, y, vh) = choice(listofwalls)
    walk(x, y, vh)
    mazeWrite(name)


num = int(input("Entrer la taille de maze: "))
name = input("Entrer le nom de maze: ")
make_maze(num, name)
