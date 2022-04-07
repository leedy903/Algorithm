import math
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

ans = 0
for i, elem in enumerate(A):
    if (elem - B > 0):
        ans = ans + math.ceil((elem - B)/C)

print(ans + N)