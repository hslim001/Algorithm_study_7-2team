N = int(input())
fields = [[0]*100 for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            fields[i][j] = 1
res = 0
for i in range(100):
    res += fields[i].count(1)
print(res)