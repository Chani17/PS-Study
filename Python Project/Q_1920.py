# 이분탐색(Binary search)
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
N_list = list(map(int, input().split()))
N_list.sort(key=lambda x:x)

input = sys.stdin.readline
M = int(input())
M_list = list(map(int, input().split()))

start = 0               # start index는 0으로 설정
end = len(N_list)-1     # end index는 list의 마지막으로 설정

def search(num, list, start, end):
    # middle index값 설정
    middle = (start + end) // 2

    # Base case
    if start > end:                 # 해당 번호가 없다면
        return 0                    # 0을 리턴
    elif list[middle] == num:                           # 해당 번호를 찾으면
        return 1                                        # 1을 리턴
    # Recursive case
    elif list[middle] > num:                            # middle index의 번호가 해당 번호보다 크다면
        return search(num, list, start, middle - 1)     # end값 = middle의 전 값
    else:                                               # middle index의 번호가 해당 번호보다 작다면
        return search(num, list, middle+1, end)         # start값 = middle의 다음 값

for number in M_list:
    print(search(number, N_list, start, end))

# Input
# 5
# 4 1 5 2 3
# 5
# 1 3 7 9 5
