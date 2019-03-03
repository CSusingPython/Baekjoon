#too easy
_, n1, n2 = map(int, input().split())
n1 -= 1
n2 -= 1
cnt = 0
while n1 != n2:
    n1 = n1 // 2
    n2 = n2 // 2
    cnt += 1
print(cnt)