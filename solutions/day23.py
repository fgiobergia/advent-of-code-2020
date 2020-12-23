class Node:
    def __init__(self, num):
        self.num = num
        self.fwd = None

def sub_circular(ch, min_val, max_val):
    if ch == min_val:
        return max_val
    return ch-1

def to_str(nodes):
    node = nodes[1]
    buf = ""
    while node.fwd.num != 1:
        node = node.fwd
        buf += str(node.num)
    return buf

def play(nodes, start, num_moves):
    curr_cup = nodes[start]
    min_val = 1
    max_val = max(nodes)

    for i in range(num_moves):
        to_move = curr_cup.fwd

        curr_cup.fwd = to_move.fwd.fwd.fwd # tg it's only 3 cups

        extracted = { to_move.num, to_move.fwd.num, to_move.fwd.fwd.num }
        next_num = sub_circular(curr_cup.num, min_val, max_val)
        while next_num in extracted:
            next_num = sub_circular(next_num, min_val, max_val)
        
        next_cup = nodes[next_num]
        to_move.fwd.fwd.fwd = next_cup.fwd
        next_cup.fwd = to_move

        curr_cup = curr_cup.fwd

def gen_nodes(input_str, tot):
    nodes = {}
    for i in range(tot):
        num = input_str[i] if i < len(input_str) else i + 1
        node = Node(num)
        if i:
            prev_node.fwd = node
        nodes[num] = node
        prev_node = node
        if i == tot-1:
            # final node wraps around to 1st
            node.fwd = nodes[input_str[0]]
    return nodes

if __name__ == "__main__":
    input_str = list(map(int,list("368195742"))) # actual input

    nodes = gen_nodes(input_str, len(input_str))
    play(nodes, input_str[0], 100)
    print(to_str(nodes))

    # exec time 20s idgaf
    nodes = gen_nodes(input_str, 1000000)
    play(nodes, input_str[0], 10000000)
    print(nodes[1].fwd.num * nodes[1].fwd.fwd.num)