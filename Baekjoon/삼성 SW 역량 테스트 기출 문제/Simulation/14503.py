import sys
N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
_map = []
for i in range(N):
    _map.append(list(map(int, sys.stdin.readline().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

cnt = 0

def cleaning(x: int, y: int, d: int) -> int:
    cnt = 0
    #global cnt
    # 현재 위치 청소
    # 2로 만든다.
    if _map[y][x] == 0:
        _map[y][x] = 2
        cnt = 1
        #cnt += 1

    # 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 차례대로 인접한 칸을 탐색
        # 왼쪽 방향에 아직 청소하지 않은 공간이 존재한다면, 그 방향으로 회전한 다음 한 칸을 전진하고 1번부터 진행
        # 왼쪽 방향에 청소할 공간이 없다면 그 방향으로 회전하고 2번으로 돌아간다.
        # 네 방향 모두 청소가 이미 되어있거나 벽인 경우에는, 바라보는 방향을 유지한 채로 한 칸을 후진하고 2번으로 돌아간다.
        # 네 방향 모두 청소가 이미 되어있거나 벽이면서, 뒤쪽 방향이 벽이라 후진도 할 수 없는 경우에는 작동을 멈춘다.

    for i in range(4):
        nd = (i + d) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]

        if nx >= 0 and ny >= 0 and nx < M and ny < N:
            if _map[ny][nx] == 0:
                cnt += cleaning(nx, ny, (nd + 3) % 4)
                return cnt
                #cleaning(nx, ny, (nd + 3) % 4)

    nd = (d + 3) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]

    if nx >= 0 and ny >= 0 and nx < M and ny < N:
        if _map[ny][nx] == 1:
            return cnt
            #return
        cnt += cleaning(nx, ny, (nd + 3) % 4)
        #cleaning(nx, ny, nd)
        return cnt

#cleaning(r, c, d)
#print(cnt)
print(cleaning(r, c, d))

'''
예제 입력 1
3 3
1 1 0
1 1 1
1 0 1
1 1 1

예제 출력 1
1

예제 입력 2
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1

예제 출력 2
57
'''