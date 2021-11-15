# 백준 1405번 미친 로봇
from itertools import product
from tqdm.auto import tqdm
base = list(map(int, input().split()))
N = base[0]
prob = base[1:]

mapping = {0: "E", 1: "W", 2: "N", 3: "S"}
go = {"E": 0, "W": 1, "N": 2, "S": 3}
direction = [mapping[i] for i in range(len(prob)) if prob[i] != 0]

def is_simple(pth):
    ckpt = [(0, 0)]
    start = (0, 0)
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for p in pth:
        nx = start[0] + dx[go[p]]
        ny = start[1] + dy[go[p]]
        new = (nx, ny)
        start = new
        if new in ckpt:
            return False
    return True

path = []
for pth in tqdm(product(direction, repeat=N)):
    if is_simple(pth):
        path.append(pth)


def get_prob(pth, prob, go):
    probability = 1
    for p in pth:
        probability *= prob[go[p]]/100
    return probability


total = 0
for p in tqdm(path):
    total += get_prob(p, prob, go)
print(f"{total:.9f}")