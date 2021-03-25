# 정렬
# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

# 수의 개수 입력
N = int(input())
number_list = []

for _ in range(N):
    number = int(input())
    number_list.append(number)

# 오름차순으로 정렬
number_list.sort(key=lambda x:x)

# 정렬한 결과를 한줄에 하나씩 출력
for num in number_list:
    print(num)

# Input
# 5
# 5
# 2
# 3
# 4
# 1