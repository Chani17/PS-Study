# 이분탐색(Binary search)
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input())
number = tuple(map(int, input().split()))
N_list = sorted(number)

M = int(input())
m_number = tuple(map(int, input().split()))
M_list = sorted(m_number)

def binary_search(element, list1, start_index=0, end_index):
    end_index = len(list1)-1
    middle_index = (start_index + end_index) // 2

    # base case
    if element == middle_index:
        return 1

    # recursive case
    if list[middle_index] > element:
        end_index = middle_index - 1
        return binary_search(element, list1, start_index, end_index)
    elif list[middle_index] < element:
        start_index = middle_index + 1
        return binary_search(element, list1, start_index, end_index)


