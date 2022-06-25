# https://www.acmicpc.net/problem/1343

data = input()
while data.count("XXXX") != 0:
    data = data.replace("XXXX", "AAAA")
while data.count("XX") != 0:
    data = data.replace("XX", "BB")
if data.count("X") != 0:
    print(-1)
else:
    print(data)
