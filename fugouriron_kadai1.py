M = 3
N = (1<<M) - 1
K = N - M
def hamming_encode(u):
    g = [0b1000111,
         0b0100101,
         0b0010011,
         0b0001110]
    w = 0
    for i in range(K):
        if ( u >> (K-1-i) ) &1 : w ^= g[i]
    return w

def hamming_decode(y):
    ht = [0b111,0b101,0b011,0b110,0b100,0b010,0b001]
    s = 0
    for i in range(N):
        if (y >> (N-1-i)) & 1: s ^= ht[i]
    print("s =",format(s,'03b'))
    if s != 0:
        y ^= ( 1 << (N-1-ht.index(s)))
        
    return y

u = 0b0000

for j in range(16):
    w = hamming_encode(u)
    print(format(w,'07b'))
    u = u + 0b001
y = w ^ ( 1 << 7 )
print(format(y,'07b'))
y = hamming_decode(y)
print(format(y,'07b'))
