# https://www.acmicpc.net/problem/1439

result = [0, 0]
last = ''
for i in input():
    if last != i:
        result[int(i)] += 1
        last = i
print(min(result))