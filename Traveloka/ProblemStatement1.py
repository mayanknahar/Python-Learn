t=int(input())
m=[]
for i in range(t):
    n=int(input())
    for i in range(n):
        e,s=input().split()
        if e=='A':
            m.append(int(s))
        elif e=='D':
            for j in range(len(m)):
                m[j]=m[j]-int(s)
        elif e=='I':
            for k in range(len(m)):
                m[k]=m[k]+int(s)
        elif e=='P':
            m=sorted(m)
            m=m[::-1]
            if m[0]==0:
                m=m
            else:
                m.insert(0,0)
            print(m[int(s)])