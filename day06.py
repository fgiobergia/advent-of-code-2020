if __name__ == "__main__":
    groups = []
    group = []
    with open("day06.input") as f:
        for line in f.readlines():
            line = line.strip()
            if line:
                group.append(set(line))
            else:
                groups.append(group)
                group = []
    if group:
        groups.append(group)
    
    print(sum([ len(set.union(*g)) for g in groups ]))
    print(sum([ len(set.intersection(*g)) for g in groups ]))