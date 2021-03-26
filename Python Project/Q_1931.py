# 한 개의 회의실이 있는데 이를 사용하고자 하는 N개의 회의에 대하여 회의실 사용표를 만들려고 한다.
# 각 회의 I에 대해 시작시간과 끝나는 시간이 주어져 있고,
# 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 회의의 최대 개수를 찾아보자.
# 단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과
# 동시에 다음 회의가 시작될 수 있다. 회의의 시작시간과 끝나는 시간이 같을 수도 있다.
# 이 경우에는 시작하자마자 끝나는 것으로 생각하면 된다.

import sys
input = sys.stdin.readline

# 총 회의의 수 입력
n = int(input())
conference = []    # 회의 정보를 담을 리스트
count = 1       # 가장 빨리 끝나는 회의는 무조건 회의실을 사용하기 때문에 count 1에서 시작

for _ in range(n):
    course = list(map(int, input().split()))
    conference.append(course)

# 끝나는 시간이 빠른 순으로 정렬, 만약 똑같은 시간에 끝나는 회의라면 먼저 시작하는 회의를 순위로 정렬
conference.sort(key=lambda x: (x[1],x[0]))

# 가장 빨리 끝나는 회의는 무조건 회의실 사용
selection = conference[0][1]

# 가장 빨리 끝나는 회의의 끝나는 시간보다 일찍 시작하면 회의실을 사용 할 수 없다.
for meeting in conference[1:]:
    if meeting[0] >= selection:
        selection = meeting[1]
        count += 1
print(count)

# 방법 2
#initial = 0
#
# for i in range(len(conference)):
#     if initial <= conference[i][0]:
#         initial = conference[i][1]
#         count += 1
# print(count)


# Input
# 11
# 1 4
# 3 5
# 0 6
# 5 7
# 3 8
# 5 9
# 6 10
# 8 11
# 8 12
# 2 13
# 12 14