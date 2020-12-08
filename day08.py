def map_instruction(string):
    instr, off = string.strip().split(" ")
    return [instr, int(off)]

def run(code):
    ptr = 0
    acc = 0
    visited = [False]*len(code)
    while ptr < len(code) and not visited[ptr]:
        visited[ptr] = True
        if code[ptr][0] == "acc":
            acc += code[ptr][1]
        elif code[ptr][0] == "jmp":
            ptr += code[ptr][1]-1 # -1 => +1 next!
        ptr += 1
    # return acc and boolean (if code ended)
    return acc, ptr==len(code)
    

if __name__ == "__main__":
    with open("day08.input") as f:
        code = [ map_instruction(line) for line in f.readlines() ]
    
    acc, _ = run(code)
    print(acc)
    swap_list = ["nop","jmp"]
    for i in range(len(code)):
        if code[i][0] in swap_list:
            code[i][0] = swap_list[1-swap_list.index(code[i][0])]
            acc, ret = run(code)
            if ret:
                print(acc)
                break
            code[i][0] = swap_list[1-swap_list.index(code[i][0])]