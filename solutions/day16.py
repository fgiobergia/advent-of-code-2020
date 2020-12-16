from functools import reduce

if __name__ == "__main__":
    with open("day16.input") as f:
        constraints = {}
        while True:
            line = f.readline()
            if not line.strip():
                break
            name, lst = line.strip().split(": ")
            constraints[name] = [ list(map(int,k.split("-"))) for k in lst.split(" or ") ]
        f.readline()
        ticket = list(map(int,f.readline().split(",")))
        [ f.readline() for _ in range(2) ]
        tickets = [ list(map(int,line.split(","))) for line in f.readlines() ]
    
    tot_sum = 0
    valid_tickets = []
    for t in tickets:
        invalid_sum = sum([ tv for tv in t if not any([ a<= tv <= b for x in constraints.values() for a,b in x]) ])
        tot_sum += invalid_sum
        if not invalid_sum:
            valid_tickets.append(t)
    print(tot_sum)

    trsp = [ [] for _ in range(len(constraints)) ]
    for t in valid_tickets:
        for i in range(len(t)):
            trsp[i].append(t[i])
    
    candidates = []
    for col in trsp:
        candidates.append([])
        for name, const in constraints.items():
            if all([ any([a <= c <= b for a,b in const ]) for c in col ]):
                candidates[-1].append(name)
    
    while not all([ len(x) == 1 for x in candidates ]):
        for i in range(len(candidates)):
            if len(candidates[i]) == 1:
                for j in range(len(candidates)):
                    if i != j and candidates[i][0] in candidates[j]:
                        candidates[j].remove(candidates[i][0])

    def reduce_departure(a,b):
        if b[0][0].startswith("departure"):
            return a * b[1]
        return a
    print(reduce(reduce_departure, zip(candidates, ticket), 1))