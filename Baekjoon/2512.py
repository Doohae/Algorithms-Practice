# 백준 2512번 예산

N = int(input())
requests = list(map(int, input().split()))
M = int(input())

start, end = 1, max(requests)*2

while start <= end:
    mid = (start + end) // 2
    total = sum([request if request <= mid else mid for request in requests])
    if total > M:
        end = mid - 1
    else:
        start = mid + 1

answer = max([request if request <= end else end for request in requests])
print(answer)
