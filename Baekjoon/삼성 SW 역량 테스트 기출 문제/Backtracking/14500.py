dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

N, M = map(int, input().split())
scores = [list(map(int, input().split())) for _ in range(N)]
visit = [[False for _ in range(M)] for _ in range(N)]
max_socre = max(map(max, scores))

total_socre = 0
def dfs(depth: int, y: int, x: int, score: int):
    global total_socre
    # 이 조건 없이 탐색할 경우 시간 초과에 걸린다. 
    # 남아있는 점수 중 최고 점수를 더해도 최고 score 보다 작은 경우 dfs를 더 진행하지 않는다.
    if total_socre >= score + max_socre * (4 - depth):
        return
    if depth == 4:
        total_socre = max(total_socre, score)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if nx >= 0 and ny >=0 and nx < M and ny < N and not visit[ny][nx]:
            # depth가 2인 경우, 즉 ㅜ 모양의 테트로미노인 경우 제자리에서 한 번 더 탐색해 주어야 하므로 dfs를 추가해준다.
            # 이때 다음 방문할 score를 미리 더해줌으로써 복잡한 코드 구현을 피할 수 있다.
            if depth == 2:
                visit[ny][nx] = True
                dfs(depth +1, y, x, score + scores[ny][nx])
                visit[ny][nx] = False
            visit[ny][nx] = True
            dfs(depth +1, ny, nx, score + scores[ny][nx])
            visit[ny][nx] = False
    

for i in range(N):
    for j in range(M):
        visit[i][j] = True
        dfs(1, i, j, scores[i][j])
        visit[i][j] = False

print(total_socre)