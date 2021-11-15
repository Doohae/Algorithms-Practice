# 백준 9095번
T = int(input())
cases = []
for _ in range(T):
    cases.append(int(input()))

def splitted(num):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    elif num == 3:
        return 4
    else:
        return splitted(num-1)+splitted(num-2)+splitted(num-3)

for case in cases:
    print(splitted(case))