# https://www.acmicpc.net/problem/10162

t = int(input())
table = [300, 60, 10]
result = [0, 0, 0]
cnt = 0
# result = 0
for i in table:
    result[cnt] = t//i
    t = t%i
    cnt += 1

if t != 0:
    print(-1)
else:
    print(result[0], result[1], result[2])
    # target = (t//300)
    # r
