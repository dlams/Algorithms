# https://www.acmicpc.net/problem/1417

import sys
data = []
for _ in range(int(input())):
    data.append(int(sys.stdin.readline()))

result = 0
while data.index(max(data)) != 0 or data.count(max(data)) > 1:

    # if data.index(max(data)) == 0:
    #     M = data.index(max(data), 1, -1)
    # else:
    M = data[1:].index(max(data)) + 1

    data[M] -= 1
    data[0] += 1
    result += 1

print(result)
