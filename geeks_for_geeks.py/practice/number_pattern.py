# n=5

# 1 121 12321 1234321 123454321

n = 5
if n == 1:
    print(1)
else:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        print()