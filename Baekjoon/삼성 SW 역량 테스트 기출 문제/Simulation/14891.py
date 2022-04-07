from collections import deque
cogwheels = [deque(list(input())) for _ in range(4)]
K = int(input())
rotations = [list(map(int, input().split())) for _ in range(K)]
rotated = [False] * 4


def rotater(cognow: int, clockwise: int) -> None:
    global  cogwheels, rotated
    if cognow < 0 or cognow > 3:
        return

    cogleft = cognow - 1
    cogright = cognow + 1

    if cogleft >= 0 and not rotated[cogleft]:
        if cogwheels[cogleft][2] != cogwheels[cognow][6]:
            rotated[cogleft] = True
            rotater(cogleft, -clockwise)
            cogwheels[cogleft].rotate(-clockwise)

    if cogright < 4 and not rotated[cogright]:
        if cogwheels[cogright][6] != cogwheels[cognow][2]:
            rotated[cogright] = True
            rotater(cogright, -clockwise)
            cogwheels[cogright].rotate(-clockwise)

for i in range(K):
    cognow, clockwise = rotations[i]
    cognow -= 1
    rotated[cognow] = True
    rotater(cognow, clockwise)
    cogwheels[cognow].rotate(clockwise)
    rotated = [False] * 4

score = 0
for i, cogwheel in enumerate(cogwheels):
    score += int(cogwheel[0]) * (2**i)

print(score)

'''
##DEBUG##
def show_cog():
    for i in range(4):
        print("  {}  ".format(cogwheels[i][0]), end=" ")
    print()
    for i in range(4):
        print(" {} {} ".format(cogwheels[i][7], cogwheels[i][1]), end=" ")
    print()
    for i in range(4):
        print("{}   {}".format(cogwheels[i][6], cogwheels[i][2]), end=" ")
    print()
    for i in range(4):
        print(" {} {} ".format(cogwheels[i][5], cogwheels[i][3]), end=" ")
    print()
    for i in range(4):
        print("  {}  ".format(cogwheels[i][4]), end=" ")
    print("\n")

for i in range(K):
    cognow, clockwise = rotations[i]
    cognow -= 1
    print("step: [{}]\nCOG:{} ROTATION: {}".format(i, cognow, clockwise))
    print("Before rotate")
    show_cog()
    rotated[cognow] = True
    rotater(cognow, clockwise)
    cogwheels[cognow].rotate(clockwise)
    rotated = [False] * 4
    print("After rotate")
    show_cog()

score = 0
for i, cogwheel in enumerate(cogwheels):
    score += int(cogwheel[0]) * (2**i)

print(score)
'''
