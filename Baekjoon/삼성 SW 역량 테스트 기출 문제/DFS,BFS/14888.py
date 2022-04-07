'''
from itertools import permutations

N = int(input())
Numbers = list(map(int, input().split()))
OperNum = list(map(int, input().split()))
OperCase = set(permutations(list('+'*OperNum[0]+'-'*OperNum[1]+'x'*OperNum[2]+'/'*OperNum[3])))
max_num = -9876543211
min_num = 9876543211

for case in OperCase:
    score = Numbers[0]
    for i, elem in enumerate(case):
        if elem == '+':
            score += Numbers[i+1]
        elif elem == '-':
            score -= Numbers[i+1]
        elif elem == 'x':
            score *= Numbers[i+1]
        elif elem == '/':
            score = int(score/Numbers[i+1])
    max_num = max(score, max_num)
    min_num = min(score, min_num)

print('{}\n{}'.format(max_num, min_num))
'''
N = int(input())
Numbers = list(map(int, input().split()))
OperNum = list(map(int, input().split()))

maximum = -987654321
minimum = 987654321

def dfs(depth, total, plus, minus, multiply, divide):
    #global N # global로 명시하여 작성해도 문제없으나 N값을 변경하지 않으므로 그냥 사용했다.
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + Numbers[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - Numbers[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * Numbers[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / Numbers[depth]), plus, minus, multiply, divide - 1)
    
dfs(1, Numbers[0], OperNum[0], OperNum[1], OperNum[2], OperNum[3])
print('{}\n{}'.format(maximum, minimum))