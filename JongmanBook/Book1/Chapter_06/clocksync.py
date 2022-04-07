SWITCHES = [[0, 1, 2],
        [3, 7, 9, 11],
        [4, 10, 14, 15],
        [0, 4, 5, 6, 7],
        [6, 7, 8, 10, 12],
        [0, 2, 14, 15],
        [3, 14, 15],
        [4, 5, 7, 14, 15],
        [1, 2, 3, 4, 5],
        [3, 4, 5, 9, 13]]


def push(clocks: list, switch: int) -> None:
    for elem in SWITCHES[switch]:
        clocks[elem] = clocks[elem] + 3
        if clocks[elem] == 15:
            clocks[elem] = 3
    
def istwelve(clocks: list) -> bool:
    for clock in clocks:
        if clock != 12:
            return False
    return True

def solve(clocks: list, switch: int) -> int:
    # base case
    if switch == 10:
        return 0 if istwelve(clocks) else INF
    
    ret = INF
    for i in range(4):
        ret = min(ret, i + solve(clocks, switch + 1))
        push(clocks, switch)

    return ret

INF = 987654321
case_num = int(input())
for _ in range(case_num):
    clocks = list(map(int, input().split()))
    print(solve(clocks, 0))