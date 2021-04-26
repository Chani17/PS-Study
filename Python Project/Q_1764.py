# 김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
# 첫째 줄에 듣도 못한 사람의 수 N, 보도 못한 사람의 수 M이 주어진다.
# 이어서 둘째 줄부터 N개의 줄에 걸쳐 듣도 못한 사람의 이름과, N+2째 줄부터 보도 못한 사람의 이름이 순서대로 주어진다.
# 이름은 띄어쓰기 없이 영어 소문자로만 이루어지며, 그 길이는 20 이하이다. N, M은 500,000 이하의 자연수이다.
# 듣도 못한 사람의 명단에는 중복되는 이름이 없으며, 보도 못한 사람의 명단도 마찬가지이다.

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
not_listen_people = set()
not_see_people = set()
count = 0
answer = []

for _ in range(N):
    L = input()
    not_listen_people.add(L.rstrip('\n'))

for _ in range(M):
    S = input()
    not_see_people.add(S.rstrip('\n'))

names = list(not_listen_people & not_see_people)           #intersection
names.sort(key=lambda x:x)

print(len(names))

for name in names:
    print(name)

# Input
# 3 4
# ohhenrie
# charlie
# baesangwook
# obama
# baesangwook
# ohhenrie
# clinton