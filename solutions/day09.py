import numpy as np

if __name__ == "__main__":
    with open("day09.input") as f:
        seq = list(map(int,f.readlines()))
    
    s = set(seq[:25]) # <= using a set to keep it O(n^2)
    for i in range(25, len(seq)):
        if not any([ seq[i]-j in s for j in s]):
            glitch = seq[i]
            print(glitch)
            break
        s.remove(seq[i-25])
        s.add(seq[i])

    cumul = np.zeros(len(seq))
    for i in range(len(seq)):
        cumul[:i+1] += seq[i]
        nz = (cumul==glitch).nonzero()[0]
        if len(nz):
            print(min(seq[nz[0]:i+1]) + max(seq[nz[0]:i+1]))
            break