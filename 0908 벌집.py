# 벌집 - 백준
# https://www.acmicpc.net/problem/2292

n = int(input())

if n==1:
    print(1)
    exit(0)

num = 0
total = 1
while True:
    if n <= total:
        break
    num += 6
    total += num
print(num//6+1)
