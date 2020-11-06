import sys

sys.setrecursionlimit(10**9)


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
            j >= 0 and j <= (len(matrix) - 1))
    backtrack(0, 0)
    if len(solution) == 0:
        print("no path found!")
    for path in solution:
        for coordonnee in path:
            (x, y) = coordonnee
            matrix[x][y] = "o"

   #  for i in range(len(matrix)):
   #      for j in range(len(matrix)):
   #          if matrix[i][j] == ".":
   #              matrix[i][j] = "*"

    for line in matrix:
        line = "".join(line)
        print(line)


name = input("Entrer le nom de maze: ")
mazesolverBacktrack(name)
