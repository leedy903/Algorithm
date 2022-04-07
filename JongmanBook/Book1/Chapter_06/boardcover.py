COVER_TYPE = (
    ((0, 0), (1, 0), (0, 1)),
    ((0, 0), (0, 1), (1, 1)),
    ((0, 0), (1, 0), (1, 1)),
    ((0, 0), (1, 0), (1, -1))
)

def setter(board: list, y: int, x: int, type: int, delta: int) -> bool:
    ok = True
    for i in range(3):
        ny = y + COVER_TYPE[type][i][0]
        nx = x + COVER_TYPE[type][i][1]
        if ny < 0 or ny >= len(board) or nx < 0 or nx >= len(board[0]):
            ok =  False
        else:
            board[ny][nx] = board[ny][nx] + delta
            if board[ny][nx] > 1:
                ok = False
    return ok


def cover(board: list) -> int:
    y, x = -1, -1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                y = i
                x = j
                break
        if y != -1:
            break
    if y == -1:
        return 1
    
    ret = 0
    for ctype in range(4):
        if setter(board, y, x, ctype, 1):
            ret += cover(board)
        setter(board, y, x, ctype, -1)
    return ret

def numberize(board: list) -> list:
    for i in range(len(board)):
        for j, elem in enumerate(board[i]):
            if elem == '#':
                board[i][j] = 1
            elif elem == '.':
                board[i][j] = 0
    return board

case_num = int(input())
for _ in range(case_num):
    H, W = map(int, input().split())
    board = [list(input()) for _ in range(H)]
    board = numberize(board)
    print(cover(board))


'''
3
3 7
#.....#
#.....#
##...##
3 7
#.....#
#.....#
##..###
8 10
##########
#........#
#........#
#........#
#........#
#........#
#........#
##########
'''
