# 백준 2667번 단지번호붙이기
from collections import deque

N = int(input())
matrix = []
for _ in range(N):
    matrix.append(list(map(int, list(input()))))

house = []
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def visit(matrix, i, j):
    que = deque([(i, j)])
    matrix[i][j] += 1
    num = 1
    while que:
        x, y = que.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix):
                continue
            if matrix[nx][ny] == 1:
                matrix[nx][ny] += 1
                que.append((nx, ny))
                num += 1
    return num

for i in range(N):
    for j in range(N):
        if matrix[i][j] == 1:
            house.append(visit(matrix, i, j))

house.sort()
print(len(house))
for h in house:
    print(h)
