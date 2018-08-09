n,m=input().split()
n,m=int(n),int(m)
for i in range(n+1,m):
    if (i<m-1):
        k=' '
    else:
        k=''
    if (i%2!=0):
        print(i,end=k)
