import sys
from collections import deque
N, L, R = map(int, sys.stdin.readline().split())
land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

def show_land() -> None:
    print("===="*N)
    for i in range(N):
        for j in range(N):
            print(" {}".format(land[i][j]), end=" ")
        print()
    print()

def bfs(x: int, y: int) -> int:
    q = deque([[y, x]])
    unions = [[y, x]]
    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if L <= abs(land[y][x] - land[ny][nx]) <= R:
                    visited[ny][nx] = True
                    q.append([ny, nx])
                    unions.append([ny, nx])
    return unions

count = 0
while True:
    isClear = True
    visited = [[False] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                visited[i][j] = True
                unions = bfs(j, i)
                if len(unions) > 1:
                    isClear = False
                    population = sum(land[x][y] for x,y in unions)//len(unions)

                    for uy, ux in unions:
                        land[uy][ux] = population    

    show_land()

    if isClear:
        print(count)
        break
            
    count += 1
