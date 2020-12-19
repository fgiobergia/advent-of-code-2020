# bau :)

class Rule:
    def __init__(self, n):
        self.n = n
        self.options = []
    
    def add_option(self, option, rule_objs):
        opt = []
        for el in option:
            opt.append(rule_objs[el] if el not in "ab" else el )
        self.options.append(opt)

def navigate(string, i, rules, curr_pos, depth=0):
    pos_list = []
    for option in rules[curr_pos].options:
        pos_stack = [(i,0)]
        while pos_stack:
            pos, j = pos_stack.pop(0)
            if j == len(option):
                pos_list.append(pos)
                continue
            if pos == len(string):
                continue
        
            el = option[j]
            if isinstance(el, str):
                success = string[pos] == el
                if success:
                    pos_stack.append((pos+1,j+1))
            else:
                poss = navigate(string, pos, rules, el.n, depth+1)
                for pos in poss:
                    pos_stack.append((pos,j+1))

    return pos_list

def is_valid(string, rules):
    b = navigate(string, 0, rules, "0")
    return any(b_ == len(string) for b_ in b)

def map_rules(rules):
    rule_objs = {rule_id: Rule(rule_id) for rule_id in rules }
    for rule_id in rules:
        for option in rules[rule_id]:
            rule_objs[rule_id].add_option(option, rule_objs)
    return rule_objs

def map_el(el):
    if el in ['"a"', '"b"']:
        return el[1]
    return el

if __name__ == "__main__":
    with open("day19.input") as f:
        rules = {}
        messages = []

        while True:
            line = f.readline().strip()
            if not line:
                break
            rule_id, options = line.split(": ")
            or_options = [ list(map(map_el, option.split(" "))) for option in options.split(" | ") ]
            rules[rule_id] = or_options
        
        messages = [line.strip() for line in f.readlines()]
        rules_obj = map_rules(rules)

        print(len([ m for m in messages if is_valid(m, rules_obj) ]))

        rules['8'] = [['42'], ['42','8']]
        rules['11'] = [['42','31'],['42','11','31']]
        rules_obj = map_rules(rules)
        print(len([ m for m in messages if is_valid(m, rules_obj) ]))