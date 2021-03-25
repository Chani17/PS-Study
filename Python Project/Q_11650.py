# 정렬
# 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

# N개의 점 입력
N = int(input())
number_list = []

# 좌표 입력
for _ in range(N):
    num1, num2 = map(int, input().split())
    number_list.append([num1, num2])

number_list.sort(key=lambda x: (x[0],x[1]))

for i in range(N):
    print(number_list[i][0], number_list[i][1])

# Input
# 5
# 3 4
# 1 1
# 1 -1
# 2 2
# 3 3