import sys
import os
import faulthandler
from PIL import Image, ImageDraw

faulthandler.enable()
os.system("cls")
sys.setrecursionlimit(10 ** 9)


def mazesolverBacktrack(name):
    matrix = []
    ListeDonees = open(f"{name}.txt").read().split()
    for ligne in ListeDonees:
        Listecaratere = []
        for caractere in ligne:
            Listecaratere.append(caractere)
        matrix.append(Listecaratere)

    visit = [[0] * len(matrix) for _ in range(len(matrix))]

    path = []

    solution = []

    rowNeighbors = [-1, 1, 0, 0]
    colNeighbors = [0, 0, 1, -1]

    def backtrack(i, j):
        while i < len(matrix)**4:
            i = i+1
            if visit[i][j] != 0 or matrix[i][j] == "#":
                return

            visit[i][j] = 1
            path.append((i, j))
            if matrix[i][j] == "." and (i, j) == ((len(matrix) - 1), (len(matrix) - 1)):
                solution.append(list(path))
                path.pop()
                return
            for k in range(4):

                nouveaui = i + rowNeighbors[k]
                nouveauj = j + colNeighbors[k]
                if valid(nouveaui, nouveauj):
                    backtrack(nouveaui, nouveauj)
            path.pop()
            return

    def valid(i, j):
        return (i >= 0 and i <= (len(matrix) - 1)) and (
            j >= 0 and j <= (len(matrix) - 1)
        )

    if len(solution) == 0:
        print("no path found!")
    for path in solution:
        for coordonnee in path:
            (x, y) = coordonnee
            # matrix[x][y] = "\u001b[31mo\u001b[37m"
            matrix[x][y] = "o"

    #  for i in range(len(matrix)):
    #      for j in range(len(matrix)):
    #          if matrix[i][j] == ".":
    #              matrix[i][j] = "*"

    for line in matrix:
        line = "".join(line)
        print(line)

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}solution.txt", "a")
        for line in matrix:
            s += "".join(line + ["\n"])
        ths.write(s)
        ths.close()
        createJPG()

    # mazeWrite(name)

    def createJPG():
        w = len(matrix)
        large = 15*(w)
        img = Image.new('RGB', (large, large), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        for y in range(w):
            for x in range(w):
                try:
                    if matrix[y][x] == "#" and y % 2 == 1:
                        draw.line((15*x, 15*(y-1), 15*x, 15*(y+1)),
                                  fill=(0, 0, 0), width=3)
                    if matrix[y][x] == "#" and y % 2 == 0 and x % 2 != 0:
                        draw.line((15*(x-1), 15*y, 15*(x+1), 15*y),
                                  fill=(0, 0, 0), width=3)
                    if matrix[y][x] == "o" and x % 2 != 0:
                        draw.rectangle((15*(x-1), 15*(y-1), 15*(x+1), 15*(y+1)),
                                       fill=(175, 0, 175), width=3)

                except:
                    pass
        img.show()
        img.save(f"{name} solution.jpg")

    def mazeWrite(name):
        s = ""
        ths = open(f"{name}solution.txt", "a")
        for line in matrix:
            s += "".join(line + ["\n"])
        ths.write(s)
        ths.close()
        createJPG()

    backtrack(0, 0)
    # print(stack)
    # print(len(stack))

    # backtracmotor()
    # debugPrint()
    mazeWrite(name)


name = input("Entrer le nom de maze: ")
mazesolverBacktrack(name)
