from random import randint
import sys

'''
    n*m
    a[i,j] = 0..9
    -> | 
    
    goto a[last][last] with lowest price
'''

def MinPrice(n,m, show = False):
    l = [[randint(0,    9) for j in range(m)] for i in range(n)]

    if show:
        for li in l: print(li)
    print()

    for i in range(1,m):
        l[0][i]+=l[0][i-1]
    for i in range(1,n):
        l[i][0]+=l[i-1][0]

    for i in range(1,n):
        for j in range(1,m):
            l[i][j] += min(l[i-1][j],l[i][j-1])


    n-=1
    m-=1

    steps = [(n,m)]
    while n>0 and m>0:
        if l[n-1][m] < l[n][m-1]:
            steps.append((n-1,m))
            n-=1
        else:
            steps.append((n,m-1))
            m-=1

    while n>=0:
        steps.append((n,m))
        n-=1
    while m>=0:
        steps.append((n,m))
        m-=1

    steps.pop()
    steps.reverse()

    print('Step by step:')
    for s in steps:
        print(s)


    print('Memory:',sys.getsizeof(l))

    return l[-1][-1]

print('Min price:',MinPrice(2,3,True))
