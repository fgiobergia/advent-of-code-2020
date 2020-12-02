from collections import Counter

if __name__ == "__main__":
    with open("day02.input") as f:
        lines = [ line.strip().split(" ") for line in f.readlines() ]

    count1 = 0 # counter for 1st policy (min-max)
    count2 = 0 # counter for 2nd policy (XOR positions)
    for ab, letter, password in lines:
        a, b = map(int, ab.split("-"))
        count1 += a <= Counter(password)[letter[0]] <= b
        count2 += (password[a-1] == letter[0]) ^ (password[b-1] == letter[0])
    print(count1)
    print(count2)