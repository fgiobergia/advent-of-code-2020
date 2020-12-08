from functools import reduce
# F: 0, B: 1
# L: 0, R: 1

def seat2bin(seq):
    maps = {
        "F": "0", "B": "1", "L": "0", "R": "1"
    }
    return reduce(lambda s, kv: s.replace(kv[0],kv[1]), maps.items(), seq)
    

if __name__ == "__main__":
    with open("day05.input") as f:
        passes = { int(seat2bin(line),2) for line in f.readlines() }
    
    max_seat = max(passes)
    print(max_seat)

    print([ seat
            for seat in range(max_seat, 1, -1)
            if seat-1 in passes and seat+1 in passes and seat not in passes
    ][0])