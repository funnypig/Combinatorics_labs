from random import randint
import time

'''
    Є стержень довж. n
    Є ціни на довжини 1,2,...
    Порізати так, щоб отримати максимальну ціну.
    
    xi: 1   2   3   4   5   6   7   8   9   10 
    yi: 1   5   8   9   10  17  17  20  24  30
    
    прибуток:
    r_n = max[1<=i<=n] (pi,r_n-i)
    
    Додаток: розріз коштує с
'''#

''' examples
    Задача про рюкзак...
    
    Відвідати міста. У кожного є пріорітет. 
    Відвідання якогось міста має певну вартість.
    Сплланувати так, щоб максимально відвітати і вкластися в задану суму
'''
def CheckTime(f, *args):
    st = time.time()
    res = f(*args)
    fin = time.time()

    return {'result':res, 'time':fin-st}

def cut(p, n):
    if n<=0:
        return 0

    _max = 0

    for i in range(0,n):
        _max = max(_max, p[i] + cut(p, n-i-1))

    return _max

def cutMemo(p, n, memo):
    if memo[n] >= 0:
        return memo[n]

    q = 0
    if n == 0:
        q = 0
    else:
        q = -100
        for i in range(1,n+1):
            q = max(q, p[i]+cutMemo(p,n-i,memo))

    memo[n] = q
    return q

def cutMemo_CutPrice(p, n,c, memo):
    if memo[n] >= 0:
        return memo[n]

    q = 0
    if n == 0:
        q = 0
    else:
        q = -100
        for i in range(1,n+1):
            q = max(q, p[i]+cutMemo(p,n-i,memo))

    memo[n] = q-c
    return q-c


n = 10
p = [1]
for i in range(1,n):
    p.append(0)
    p[i] = p[i-1] + randint(1,5)
print(p)

#res = CheckTime(cut, p, n)
res = CheckTime(cutMemo, p, n-1, (n+1)*[-1])
print(res)

res = CheckTime(cutMemo_CutPrice, p, 1, n-1, (n+1)*[-1])



print(res)
