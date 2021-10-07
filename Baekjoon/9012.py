N = int(input())

parens = [input() for _ in range(N)]

def valid_par(par):
    stack = []
    for p in par:
        if p == '(':
            stack.append(p)
        elif p == ')':
            if len(stack) == 0:
                return 'NO'
            stack.pop()
    return 'YES' if len(stack) == 0 else 'NO'

for par in parens:
    print(valid_par(par))