''''''
'''
    Пошук максимальної підпослідовності двох послідовностей - LCS
    
    x = (x1, ..., xn)
    z = {z1, ..., zk}, zi in x
    
    Theorem 1:
    x = (x1, ..., xm)
    y = (y1, ..., yn)
    let z = {z1, ..., zk} - LCS of x, y
    
    1. if xm = yn => zk = xm = yn
        => z n-1 = LCS(x m-1, y n-1)
    2. xm != yn; zk != xm => z = LCS(x m-1, y)
    3. xm != yn; zk != yn => z = LCS(x, y n-1)
    end.
    
    Xi, Yj, i,j>0
    r[p,i] c[i,j] m[i,j] 
    
    c[i,j] = 0, i=0 or j=0
             c[i-1,j-1]+1, i,j>0 and xi=yj
             max(c[i,j-1],c[i-1,j], xi != yj
    
    TASK:
'''

def RLCS(x,y, res = ''):
    if len(x) == 0 and len(y) == 0:
        return res

    if len(x) == 0: RLCS(x,y[1:],res)
    else:
        if len(y) == 0: RLCS(x[1:],y,res)

    if len(x)!=0 and len(y)!=0 and x[0] == y[0]:
        return RLCS(x[1:],y[1:],res + x[0])
    else:
        if len(x)!=0:
            RLCS(x[1:],y, res)
        if len(y)!=0:
            RLCS(x,y[1:], res)
    return res

def LCS(x,y,c):
    res = ''
    for i in range(len(x)):
        for j in range(len(y)):
            if i == 0 and j == 0:
                c[i][j]=0

            if x[i]==y[j]:
                c[i][j] = c[i-1][j-1] + 1
                res+=x[i]
                break
            else:
                c[i][j] = max(c[i-1][j],c[i][j-1])
    return res

x = ['a','b','c','a','d']
y = ['b','c','b','d','b','c','d']

print(x)
print(y)
print()

c = [[0]*len(y)]*len(x)

print(LCS(x,y,c))
print(max(max(c)))

print('Recursion:')
#print(RLCS(x,y))
