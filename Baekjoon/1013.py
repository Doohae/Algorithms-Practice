import re

def isVega(signal):
    vega = re.compile('(100+1+|01)+')
    is_right = re.sub(vega, '', signal)
    if is_right == "":
        return 'YES'
    return 'NO'

N = int(input())
patterns = []
for _ in range(N):
    case = input().split()
    patterns.extend(case)

for i in range(N):
    print(isVega(patterns[i]))