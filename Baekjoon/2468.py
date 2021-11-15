# 백준 2468번 안전 영역
from collections import deque

N = int(input())
area = []
low, high = 0, 0
for _ in range(N):
    row = list(map(int, input().split()))
    low, high = min(min(row), low), max(max(row), high)
    area.append(row)

def water(matrix, refer, i, j):
    que = deque([(i, j)])
    refer[i][j] = True
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    while que:
        x, y = que.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix):
                continue
            if refer[nx][ny] is False:
                refer[nx][ny] = True
                que.append((nx, ny))
    return refer

results = 0
for idx in range(low, high+1):
    refer = [[False for _ in range(N)] for _ in range(N)]
    current_cnt = 0
    for i in range(N):
        for j in range(N):
            if area[i][j] <= idx and refer[i][j] is False:
                refer[i][j] = True
                continue
            if refer[i][j] is False:
                refer = water(area, refer, i, j)
                current_cnt += 1
    results = max(results, current_cnt)

print(results)
