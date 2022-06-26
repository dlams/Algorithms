# https://www.acmicpc.net/problem/1026

data = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
b.reverse()

result = 0
for i in range(data):
    result += a[i]*b[i]
print(result)