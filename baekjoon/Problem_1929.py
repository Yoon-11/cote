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

M, N = map(int, input().split())

for i in range(M, N+1):
    if i == 1:
        continue

    for k in range(2, int(i**0.5) +1):
        if i % k == 0 :
            break
    else:
        print(i)

