# 2346 풍선 터뜨리기

N = int(input())
balloons = list(map(int, input().split()))

ord = range(N)
exploded = [False]*N
result = []
while False in exploded:
    if True not in exploded:
        idx = 0
    exploded[idx] = True
    move = balloons[idx]
    for _ in range(idx+1, idx+move+1):
        