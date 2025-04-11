# 소수 구하기

# 시간 초과
# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     count = 0
#     for k in range(1, int(i**0.5) +1):
#         if i % k == 0 :
#             count += 1
#     if count == 1:
#         print(i)

# M, N = map(int, input().split())
#
# for i in range(M, N+1):
#     if i == 1:
#         continue
#
#     for k in range(2, int(i**0.5) +1):
#         if i % k == 0 :
#             break
#     else:
#         print(i)

# 에라토스테네스의 체
from math import sqrt

M, N = map(int, input().split())
is_prime = [True] * (N + 1)

is_prime[0] = is_prime[1] = False


for i in range(2, int(sqrt(N)) + 1):
    if not is_prime[i]:
        continue

    for j in range(i * i, N + 1, i):
        is_prime[j] = False


for i in range(M, N + 1):
    if is_prime[i]:
        print(i)

