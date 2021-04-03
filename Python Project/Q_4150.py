# 피보나치 수열은 다음과 같이 그 전 두 항의 합으로 계산되는 수열이다. 첫 두 항은 1로 정의된다.
# f(1) = 1, f(2) = 1, f(n > 2) = f(n − 1) + f(n − 2)
# 정수를 입력받아, 그에 해당하는 피보나치 수를 출력하는 프로그램을 작성하여라.

N = int(input())

first = 1
second = 1
temp = 0

for _ in range(N-2):
    temp = first + second
    first, second = second, temp

print(second)
