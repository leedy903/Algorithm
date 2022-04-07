N = int(input())
Map = [[0 for _ in range(N+2)] for _ in range(N+2)]
for i in range(N+2):
    Map[0][i] = -1
    Map[N+1][i] = -1
    Map[i][0] = -1
    Map[i][N+1] = -1

K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    Map[x][y] = 1

L = int(input())
Time = [0 for _ in range(L)]
Direction = [0 for _ in range(L)]

for i in range(L):
    Time[i], Direction[i] = input().split()
Time = list(map(int, Time))

i, j, ti, tj = 1, 1, 1, 1
move = [0]
my = [0, 0, -1, 1]
mx = [1, -1, 0, 0]
step = 0
bodyLength = 1
Map[i][j] = -1

while True:
    step += 1

    # head move
    i += my[move[step-1]]
    j += mx[move[step-1]]

    # Case End
    if Map[i][j] == -1:
        ans = step
        break
    # Case Apple -> Don't move the tail, Increase bodyLength
    if Map[i][j] == 1:
        bodyLength += 1
    # Case Normal
    elif Map[i][j] == 0:
        # tail move -> tail must follow the body, Don't follow the head
        Map[ti][tj] = 0
        ti += my[move[step-bodyLength]]
        tj += mx[move[step-bodyLength]]

    Map[i][j] = -1

    # Change Direction
    if step in Time:
        D = Direction[Time.index(step)]
        if (move[step-1] == 0 and D == 'D') or (move[step-1] == 1 and D == 'L'):
            move.append(3)
        elif (move[step-1] == 1 and D == 'D') or (move[step-1] == 0 and D == 'L'):
            move.append(2)
        elif (move[step-1] == 3 and D == 'D') or (move[step-1] == 2 and D == 'L'):
            move.append(1)
        elif (move[step-1] == 2 and D == 'D') or (move[step-1] == 3 and D == 'L'):
            move.append(0)
    else:
        move.append(move[-1])


print(ans)