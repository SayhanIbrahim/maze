from random import shuffle, randrange
import sys

sys.setrecursionlimit(170000)


def make_maze(num, name):
    w = num
    vis = [[0] * w + [1] for _ in range(w)] + [[1] * (w + 1)]
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

    def walk(x, y):
        m = w*w
        i = 0
        while i < m:
            vis[y][x] = 1
            d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
            shuffle(d)
            for (xx, yy) in d:
                if vis[yy][xx]:
                    continue
                if xx == x:
                    hor[max(y, yy)][x] = "#."
                if yy == y:
                    ver[y][max(x, xx)] = ".."
                x = xx
                y = yy
            i = i+1


# def go_pasrec(x, y, maze, size):
    # stack = []
    # stack.append([x, y])
    # while (len(stack) > 0):
    #     x = stack[-1][0]
    #     y = stack[-1][1]
    #     newcell = go(x, y, maze, size)
    #     if (len(newcell) > 0):
    #         stack.append(newcell)
    #     else:
    #         stack.pop()


    def mazeWrite(name):
        s = ""
        ths = open(f"{name}.txt", "a")
        for (a, b) in zip(hor, ver):
            s += "".join(a + ["\n"] + b + ["\n"])
        ths.write(s)
        ths.close()

    walk(randrange(w), randrange(w))
    debugPrint()
    mazeWrite(name)


num = int(input("Entrer la taille de maze: "))
name = input("Entrer le nom de maze: ")
make_maze(num, name)
