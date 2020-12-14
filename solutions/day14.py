if __name__ == "__main__":
    with open("day14.input") as f:
        instructions = [ line.strip().split(" = ") for line in f.readlines() ]
    
    mem = {}
    for tgt, val in instructions:
        if tgt == "mask":
            mask_or = sum([ 2**(35-i) for i in range(len(val)) if val[i] == "1" ])
            mask_and = sum([ 2**(35-i) for i in range(len(val)) if val[i] != "0" ])
        else:
            address = int(tgt[4:-1])
            mem[address] = (int(val) & mask_and) | mask_or
    print(sum(mem.values()))

    """
    This started with a clever approach to not memorize all memory addresses,
    but it turns out that the solution would get overly complicated. E.g. example below:

    mask = 000000000000000000000000000000000X00
    mem[0] = 1
    mask = 000000000000000000000000000000000100
    mem[0] = 2
    mask = 000000000000000000000000000000000100
    mem[0] = 4

    Some good old "generate all" approach has been adopted instead (there are at most 9
    X's in the masks (=> 512 addresses addressed at a time, this is quite feasible))
    """
    values = {}
    for tgt, val in instructions:
        if tgt == "mask":
            mask = [ int(x) if x != "X" else "X" for x in val ]
        else:
            base_addr = int(tgt[4:-1])
            address = [ mask[i] if mask[i] != 0 else (base_addr >> (35-i)) & 1 for i in range(36) ]
            max_len = address.count("X")
            for i in range(2**max_len):
                a = 0
                addr = 0
                for f in range(len(address)):
                    if address[f] == "X":
                        addr = (addr << 1) | ((i >> a) & 1)
                        a += 1
                    else:
                        addr = (addr << 1) | int(address[f])
                values[addr] = int(val)
    print(sum(values.values()))