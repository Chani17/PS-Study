# Greedy Algorithm
# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만드려고 한다.
# 이때 필요한 동전의 개수의 최솟값을 구하는 프로그램을 작성해라.

import sys
input = sys.stdin.readline

coin_type = []
coin_num, won = map(int, input().split())

for _ in range(coin_num):
    coin = int(input())
    coin_type.append(coin)





