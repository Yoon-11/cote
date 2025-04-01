# def likeFibo(n):
#     size = max(3, n+1)
#     array = [0]*size
#
#     array[0] = array[1] = array[2] = 1
#
#     for i in range(3, n+1):
#         array[i] = array[i-1] + array[i-3]
#
#     return array[n-1]
#
#
# n = int(input())
#
# print(likeFibo(n))


# 재귀 + 메모이제이션
def likeFibo(n, memo = None):
    if memo is None:
        memo = [-1] * (n+1)

    if n == 0 or n == 1 or n == 2:
        return 1

    if memo[n] != -1:
        return memo[n]


    memo[n] = likeFibo(n-1, memo) + likeFibo(n-3, memo)
    return memo[n]

n = int(input())
print(likeFibo(n-1))
