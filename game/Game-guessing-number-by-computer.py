import random
min=1
max=99
while True:
    guss=int((min+max)/2)
    print("My guss",guss)
    javab=str(input())
    if javab=="b":
        min=guss+1
    elif javab=="k":
        max=guss-1
    elif javab=="d":
        break
print("You Win The Game")