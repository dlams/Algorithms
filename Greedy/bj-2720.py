# https://www.acmicpc.net/problem/2720

for _ in range(int(input())):
    money = int(input())
    print(money//25, money%25//10, money%25%10//5, money%25%10%5)