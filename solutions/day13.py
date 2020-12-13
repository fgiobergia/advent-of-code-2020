from functools import reduce

def chinese(n,a):
    """
    * Chinese remainder theorem
    https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    (ni are coprimes), if Ni = prod_{j!=i}(nj),
    we can find Mi,mi s.t. (Extended Euclidean algorithm -- see below)
    Ni*Mi + ni*mi = 1
    Then, x (solution) can be written as:
    x = sum_{i}(ai*Ni*Mi)
    
    * Extended Euclidean algorithm
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
    Ni*Mi+ni*mi=1 -> Mi is the inverse of Ni (mod ni)
    """
    x = 0
    N = reduce(lambda a,b: a * b, n)
    for i in range(len(n)):
        Ni = N//n[i]
        Mi = invmod(Ni,n[i])
        x += a[i] * Ni * Mi
    return x % N

def invmod(a,b):
    # naive approach, but it works :)
    for i in range(b):
        if (a * i) % b == 1:
            return i
    
if __name__ == "__main__":
    with open("day13.input") as f:
        ts = int(f.readline())
        buses = [ int(x) if x!="x" else x for x in f.readline().split(",") ]
    valid = [ b for b in buses if isinstance(b,int) ]

wait, bus = min((((ts//b+1)*b-ts, b) for b in valid), key=lambda x: x[0])
print(wait * bus)

a = [ b-i for i,b in enumerate(buses) if isinstance(b, int) ]
print(chinese(valid, a))
