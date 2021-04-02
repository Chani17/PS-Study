# 에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾는 유명한 알고리즘이다.
# 2부터 N까지 모든 정수를 적는다.
# 아직 지우지 않은 수 중 가장 작은 수를 찾는다. 이것을 P라고 하고, 이 수는 소수이다.
# P를 지우고, 아직 지우지 않은 P의 배수를 크기 순서대로 지운다.
# 아직 모든 수를 지우지 않았다면, 다시 2번 단계로 간다.
# N, K가 주어졌을 때, K번째 지우는 수를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def Eratosthenes(number_list, key):
    count = 0
    while len(number_list) != 0:
        p = min(number_list)            # 가장 작은 수를 찾는다
        if (count + 1) == key:          # 이번에 지워야할 수가 key값(순서)과 같다면
            return p                    # 지워야할 수 return
        number_list.remove(p)           # 이번에 지워야할 수가 key값(순서)와 같지 않다면
        count += 1                      # 지워주고 count값 증가
        i = 0

        while i < len(number_list):
            if number_list[i] % p == 0:             # p의 배수이면
                if (count+1) == key:                # 이번에 지워야할 수가 key값(순서)과 같다면
                    return number_list[i]           # 지워야할 수 return
                number_list.remove(number_list[i])  # 이번에 지워야할 수가 key값(순서)과 같지 않다면
                count += 1                          # 지워주고 count값 증가
                i -= 1                              # 리스트에서 요소를 제거해줬기 때문에 순서가 밀리지 않도록 i값 조정
            i += 1

N, K = map(int, input().split())
number = []

for num in range(2, N+1):               # 2부터 N까지의 수 리스트로 만들기
    number.append(num)

print(Eratosthenes(number, K))

# Input
# 10 7