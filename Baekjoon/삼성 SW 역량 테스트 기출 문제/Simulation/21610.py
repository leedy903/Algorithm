import sys
N, M = map(int, sys.stdin.readline().split())
baskets = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

# 첫 구름 영역 생성
clouds = [[N - 1, 0], [N - 1, 1], [N - 2, 0], [N - 2, 1]]

for d, s in commands:

    # 구름 이동
        # 경계를 넘어가면 반대쪽에서 등장

    for i, cloud in enumerate(clouds):        
        cy, cx = cloud
        clouds[i] = [(cy + dy[d - 1] * s) % N, (cx + dx[d - 1] * s) % N]


    rained = [[False] * N for _ in range(N)]
    # 구름에서 비가 내려 칸의 바구니에 저장된 물의 양 1 증가
    for cy, cx in clouds:
        baskets[cy][cx] += 1
        rained[cy][cx] = True

    # 비가 내린 칸에 물복사버그 시전
        # 대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼 바구니의 물의 양이 증가
        # 이때 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
    
    for cy, cx in clouds:
        has_water = 0
        for i in range(1, 8, 2):
            ny = cy + dy[i]
            nx = cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N:
                if baskets[ny][nx] > 0:
                    has_water += 1
        baskets[cy][cx] += has_water

    new_clouds = []
    # 바구니에 저장된 물의 양이 2이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다. 이때 구름이 생기는 칸은 비가 내린칸이 아니여야한다.
    for i in range(N):
        for j in range(N):
            if baskets[i][j] > 1 and not rained[i][j]:
                new_clouds.append([i, j])
                baskets[i][j] -= 2

    clouds = new_clouds

# M번의 이동이 끝난 후 바구니에 들어있는 물의 양의 합을 출력
water = 0
for i in range(N):
    for j in range(N):
        water += baskets[i][j]

'''
# TEST
def show_clouds():
    print("==CLOUD==")
    for i in range(N):
        for j in range(N):
            if [i, j] in clouds:
                print("c", end=" ")
            else:
                print("b", end=" ")
        print()
    print()

def show_baskets():
    print("==BASKET==")
    for i in range(N):
        for j in range(N):
            print(baskets[i][j], end=" ")
        print()
    print()
print(water)
'''