# 암호 만들기
from itertools import combinations

l, c = map(int, input().split())
lst = list(map(str, input().split()))
lst.sort()

for i in combinations(lst, l):
    for u in i:
        print(u, end='')
    print()
