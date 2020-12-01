from itertools import combinations

if __name__ == "__main__":
    with open("day1.input") as f:
        entries = set(map(int, f.readlines()))
    mul = [ e for e in entries if 2020-e in entries ]
    print(mul[0]*mul[1])

    mul = [ (a,b, 2020-a-b) for a,b in combinations(entries,2) if 2020-a-b in entries ][0]
    print(mul[0]*mul[1]*mul[2])