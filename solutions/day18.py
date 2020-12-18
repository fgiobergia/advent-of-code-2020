# precedence = True: + before *, False: no precedence (parse order)
def parse(exp, i, stack, precedence):
    if i == len(exp) and len(stack)==1:
        return stack[0]
    if len(stack) >= 3:
        new_val = None
        # num + num in stack
        if isinstance(stack[-1],int) and stack[-2] == "+" and isinstance(stack[-3],int):
            new_val = stack[-1] + stack[-3]
        # num * num in stack and next comes a ) or EndOfExpression
        elif isinstance(stack[-1],int) and stack[-2] == "*" and isinstance(stack[-3],int) and (not precedence or i==len(exp) or exp[i]==")"):
            new_val = stack[-1] * stack[-3]
        if stack[-1] == ")" and isinstance(stack[-2],int) and stack[-3] == "(":
            new_val = stack[-2]
        if new_val is not None:
            stack = stack[:-3] + [new_val]
            return parse(exp,i,stack,precedence)
    # else, move along i
    stack.append(exp[i])
    return parse(exp,i+1,stack,precedence)

def read_value(v):
    if "0" <= v <= "9":
        return int(v)
    return v

# for the lulz
def sol2_lulz(ex):
    class MyInt:
        def __init__(self,a):
            self.a = a
        def __add__(self,oth):
            return MyInt(self.a*oth.a)
        def __mul__(self,oth):
            return MyInt(self.a+oth.a)
    import re
    return eval(
        re.sub("\+|\*", lambda x: "*+"[x.group(0)=="*"],
        re.sub(r"(?<=\d)", ")",
        re.sub(r"(?=\d)","MyInt("," ".join(map(str,ex)))))
    ).a
    

if __name__ == "__main__":
    with open("day18.input") as f:
        expressions = [ list(map(read_value,line.strip().replace(" ",""))) for line in f.readlines() ]
    
    print(sum(map(lambda e: parse(e,0,[],False), expressions)))
    print(sum(map(lambda e: parse(e,0,[],True), expressions)))
    print(sum(map(sol2_lulz, expressions)))