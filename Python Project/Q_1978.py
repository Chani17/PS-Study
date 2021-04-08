# 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.
# 소수 : 1보다 큰 자연수 중 1과 자기 자신만을 약수로 가지는 수

import sys
input = sys.stdin.readline

def isPrime(num):
    if num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False
    return True

N = int(input())
number = list(map(int, input().split()))

count = 0

for num in number:
    if isPrime(num):
        count += 1
print(count)


# Input
# 4
# 1 3 5 7