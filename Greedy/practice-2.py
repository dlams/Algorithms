# 각 자리가 숫자(0-9)로만 이루어진 문자열 S가 주어졌을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자ㅏ를 확인하며 숫자 사이에 'x' 또는 '+' 연산자를 넣어 결과적으로 만들어질 수 있는 가장 ㅡㄴ 수를ㄹ 구하는 프로그램을 작성하세요.
# 단, +보다 x를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서부터 순서대로 이루어진다고 가정함.

data = input()
result = int(data[0])

for i in range(1, len(data)):
    num = int(data[i])
    if num > 1 and result > 1:
        result *= num
    else:
        result += num
print(result)