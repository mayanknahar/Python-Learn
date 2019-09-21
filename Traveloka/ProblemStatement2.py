def solve(s,n):
    l=list(s)
    m=[]
    for i in range(len(l)):
        m.append(i)
    m=m[::-1]
    return m

t=int(input())
for _ in range(t):
    n=int(input())
    s=map(int, input().split())
    out=solve(s,n)
    print(' '.join(map(str,out)))
