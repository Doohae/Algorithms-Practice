# 백준 17451 평행우주

N = int(input())
planets = list(map(int, input().split()))
answer = 1
for planet in planets[::-1]:
    if answer//planet != answer/planet:
        answer = (answer//planet + 1)*planet
print(answer)
