# 백준 2606번 바이러스
from collections import deque

N = int(input())
M = int(input())
network = [[False]*(N+1) for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    x, y = tuple(map(int, input().split()))
    network[x][y], network[y][x] = True, True

def bfs(num):
    connect_cnt = 0
    visited[num] = True
    now = deque([num])
    while now:
        exp = now.popleft()
        connect_cnt += 1
        for i in range(1, len(network[exp])):
            if visited[i] is False and network[exp][i] is True:
                now.append(i)
                visited[i] = True
    return connect_cnt-1

print(bfs(1))