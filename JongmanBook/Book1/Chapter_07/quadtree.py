def reverse(it: int):
    it = it + 1
    if quadtree[it] == 'w' or quadtree == 'b':
        return quadtree[it]
    UL = reverse(it)
    UR = reverse(it)
    LL = reverse(it)
    LR = reverse(it)
    
    return "x"+LL+LR+UL+UR

case_num = int(input())

for _ in range(case_num):
    global quadtree
    quadtree = input()
    print(reverse(-1))