# 백준 10026번 적록색약
from collections import deque

N = int(input())
diff_image = []
same_image = []
for _ in range(N):
    line = list(input())
    diff_image.append(line)
    same_image.append([c if c in ["R", "B"] else "R" for c in line])

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(matrix, i, j, num):
    color = matrix[i][j]
    que = deque([(i, j)])
    matrix[i][j] = "Done"
    while que:
        x, y = que.popleft()
        for m in move:
            nx = x + m[0]
            ny = y + m[1]
            if nx < 0 or ny < 0 or nx >= len(matrix) or ny >= len(matrix):
                continue
            if matrix[nx][ny] == color:
                matrix[nx][ny] = "Done"
                que.append((nx, ny))
    num += 1
    return num


diff, same = 0, 0
for i in range(N):
    for j in range(N):
        if diff_image[i][j] != "Done":
            diff = bfs(diff_image, i, j, diff)
        if same_image[i][j] != "Done":
            same = bfs(same_image, i, j, same)
print(diff, same)
