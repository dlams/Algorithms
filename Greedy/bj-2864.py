# https://www.acmicpc.net/problem/2864

cnt = int(input())
data = input()
result = len(data) - data.count("LL") + 1
print(cnt if cnt <= result else result)