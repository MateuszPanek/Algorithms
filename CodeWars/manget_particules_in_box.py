"""
Solution for the following kata :
https://www.codewars.com/kata/magnet-particules-in-boxes/solutions/python
for each k in range(1, k) :
 for each n in range (1,n)V(k,n) = 1/k(n+1)**2k

"""
def doubles(maxk, maxn):
    s = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            s += 1 / (k * (n + 1)**(2 * k))
    return s


"""
Interesting solutions I found after passing kata :

def doubles(maxk, maxn):
    return sum(sum((n+1)**(-2*k)/k for n in range(1, maxn+1)) for k in range(1, maxk+1))
"""