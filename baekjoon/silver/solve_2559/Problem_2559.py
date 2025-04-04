# 수열

# 시간초과
N, K = map(int, input().split())
tmp_list = list(map(int, input().split()))

result = []

for i in range(0, len(tmp_list) -K +1):
    list_sum = 0
    front_pointer = i
    after_pointer = front_pointer + K

    slice_tmp_list = tmp_list[front_pointer:after_pointer]

    result.append(sum(slice_tmp_list))
    after_pointer += 1


print(max(result))
