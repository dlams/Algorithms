# https://www.acmicpc.net/problem/2864

a, b = input().split()

min_a, min_b = a.replace('6', '5'), b.replace('6', '5')
max_a, max_b = a.replace('5', '6'), b.replace('5', '6')
print(int(min_a)+int(min_b), int(max_a)+int(max_b))