# N = 3
# 333222111 $332211 $321 $

    
n = 10

for i in range(n,0,-1):
    for j in range(n,0,-1):
        for k in range(i,0,-1):
            print(j, end=" ")
    print("$", end="")
    if i == 1:
        print()
        

