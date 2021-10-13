# 백준 2805 나무 자르기

N, M = tuple(map(int, input().split()))
trees = list(map(int, input().split()))

mx, mn = max(trees)*2, 0

while mx >= mn:
    cut = (mx + mn) // 2
    total = sum([tree - cut for tree in trees if cut < tree])
    if total < M:
        mx = cut - 1
    else:
        mn = cut + 1
print(mx)



