from random import shuffle, randrange


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

    def walk(x, y):
        vis[y][x] = 1
        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                print(vis[yy][xx])
                continue
            if xx == x:
                hor[max(y, yy)][x] = "#."
            if yy == y:
                ver[y][max(x, xx)] = ".."

            walk(xx, yy)

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += ''.join(a + ['\n'] + b + ['\n'])
        ths.write(s)
        ths.close()

    walk(randrange(w), randrange(w))
    debugPrint()
    mazeWrite(name)


num = int(input('Entrer la taille de maze: '))
name = input('Entrer le nom de maze: ')
make_maze(num, name)
