n,m=input().split()
n=int(n)
m=int(m)
for i in range(n+1,m):
    count=0
    for j in range(1,i):
        if(i % j) == 0:
            count+=1
            if(count == 2):
                break
    else:
        if(j < n+4):
            k=' '
        else:
            k=''
        print(j+1,end=k)
