n = 10
areFriends = [[None for _ in range(10)] for _ in range(10)]

def countParings(taken: bool) -> int:
    firstFree = -1
    for i in range(0, n):
        if not taken[i]:
            firstFree = i
            break
    
    if firstFree == -1: return -1
    ret = 0
    for pairWith in range(firstFree, n):
        if not taken[pairWith] and areFriends[firstFree][pairWith]:
            taken[firstFree] = taken[pairWith] = True
            ret = ret + countParings(taken)
            taken[firstFree] = taken[pairWith] = False
    return ret

ques = '''
3
2 1
0 1
4 6
0 1 1 2 2 3 3 0 0 2 1 3
6 10
0 1 0 2 1 2 1 3 1 4 2 3 2 4 3 4 3 5 4 5 
'''



ques_num = int(input())
ques_cond = [[input().split()] for _ in range(ques_num*2)]

print(ques_cond)
# print(countParings())
