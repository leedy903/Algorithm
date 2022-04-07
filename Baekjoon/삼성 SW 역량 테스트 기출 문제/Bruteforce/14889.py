'''
import itertools

N = int(input())
S = [[] for _ in range(N)]
mans = [i for i in range(N)]
min_gap = 987654321

for i in range(N):
    S[i] = list(map(int, input().split()))

combination = list(itertools.combinations(mans, N//2))

for i in range(len(combination)//2):
    start = list(combination[i])
    link = mans[:]

    for j in range(len(start)):
        link.remove(start[j])

    start = list(itertools.permutations(start, 2))
    link = list(itertools.permutations(link, 2))

    start_score = 0
    for a, b in start:
        start_score += S[a][b]
    
    link_score = 0
    for a, b in link:
        link_score += S[a][b]

    min_gap = min(min_gap, abs(start_score - link_score))
print(min_gap)
'''
from itertools import combinations
from itertools import permutations

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
min_gap = 987654321

combination = list(combinations(list(range(N)), N//2))
combLen = len(combination)

for i in range(combLen//2):
    start = list(permutations(list(combination[i]), 2))
    link = list(permutations(list(combination[combLen - i - 1]), 2))

    start_score = link_score = 0

    for a, b in start:
        start_score += S[a][b]

    for a, b in link:
        link_score += S[a][b]

    min_gap = min(min_gap, abs(start_score - link_score))
print(min_gap)
