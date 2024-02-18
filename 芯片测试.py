n = int(input("芯片个数："))
a = [list(map(int,input().split())) for i in range(n)]
temp = [True]*n
for i in range(n):
    count = 0
    for j in range(n):
        if a[i][j]==0:
            count+=1
        if count>= n/2:
            temp[i] = False
            break
print(temp)
for i in range(n):
    if temp[i] == True:
        print(i+1,end=" ")